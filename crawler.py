import requests
from urllib.request import urlparse
from bs4 import BeautifulSoup
import re
from datetime import datetime
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import threading
import signal
import argparse

DEFAULT_CRAWL_COUNT = 100  # default number of pages to crawl
DEFAULT_MAX_WORKERS = 20  # default number of workers for thread pool


class MyCrawler:
    """ Crawler that crawls web pages starting from given seed URLs using BFS """

    def __init__(self, seeds, max_workers):
        # visited URLs
        self.__visited = []
        # unvisited URLs
        self.__unvisited = Queue()
        # number of URLs crawled
        self.__crawl_count = 0
        # number of worker threads
        self.__max_workers = max_workers
        # log file
        self.__log = open('WebCrawler_{}.txt'.format(datetime.now().strftime('%Y%m%d-%H%M%S')), 'a')
        # lock to guard the log and stdout when multiple threads write to
        self.__lock = threading.Lock()

        # add seed urls into __unvisited
        for seed in seeds:
            if self.__is_valid_url(seed):
                self.__unvisited.put(seed)

    def crawl(self, crawl_count):
        """ Start crawling
        Args:
            crawl_count: number of URLs to crawl
        """
        # keep crawling until user stops the program by CTRL-C OR the number of pages crawled equals to the specified count
        while not g_stop.is_set() and self.__crawl_count < crawl_count:
            try:
                # get a url from the queue of unvisited urls
                target_url = self.__unvisited.get(timeout=60)
                if target_url not in self.__visited:
                    # if the url is not visited yet, add it into the list of visited urls
                    self.__visited.append(target_url)
                    # increment count by 1
                    self.__crawl_count += 1
                    with ThreadPoolExecutor(self.__max_workers) as executor:
                        # schedule to request the url
                        future = executor.submit(self.__get_page, target_url)
                        # scrape the page once the request is done
                        future.add_done_callback(self.__scrape_page)
            except Queue.Empty:
                return
            except Exception as e:
                print(e)
                continue

    def __get_page(self, url):
        """ Get page with given url
        Args:
            url: URL
        Return:
            Future object
        """
        try:
            # request web page
            res = requests.get(url)
            res.raise_for_status()
            return res
        except Exception as e:
            print(e)
            return

    def __scrape_page(self, future):
        """ Scrape page
        Args:
            future: Future object to which this function attaches
        """
        # retrieve response (to the URL request) from future
        result = future.result()
        # parse the page, get absolute links from all <a href> tags, put links into the queue of unvisited urls
        if result and result.status_code == 200:
            soup = BeautifulSoup(result.text, 'lxml')
            anchors = soup.find_all('a', attrs={'href': re.compile('^https?://')})
            self.__lock.acquire()
            print(result.url)
            self.__log.write(result.url + '\n')
            for anchor in anchors:
                href = anchor['href']
                if self.__is_valid_url(href) and href not in self.__visited:
                    print(' ' + href)
                    self.__log.write(' ' + href + '\n')
                    self.__unvisited.put(href)
            self.__lock.release()

    def __is_valid_url(self, url):
        """
        Checks whether `url` is valid or not
        """
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https'] and bool(parsed.netloc)

    def __del__(self):
        if self.__log:
            self.__log.flush()
            self.__log.close()


def keyboardInterruptHandler(signal, frame):
    """ Keyboard interrupt handler """
    # set event to stop crawling
    g_stop.set()


def parse_commandline():
    """ Parse commandline arguments """
    # create parser, a ArgumentParser object
    parser = argparse.ArgumentParser(description=__doc__)
    # add arguments
    parser.add_argument('seeds', metavar='seed url', type=str, nargs='+', help='seed urls (separated by space)')
    parser.add_argument('-c', '--count', type=int, default=DEFAULT_CRAWL_COUNT, help='number of pages to crawl')
    parser.add_argument('-w', '--workers', type=int, default=DEFAULT_MAX_WORKERS, help='number of worker threads')
    # parse arguments
    return parser.parse_args()


# stop crawling when g_stop, an Event object, is set
g_stop = threading.Event()


if __name__ == '__main__':
    # Register handler for CTRL-C
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    # Parse commandline arguments
    args = parse_commandline()
    if args.count <= 0:
        args.count = DEFAULT_CRAWL_COUNT
    if args.workers <= 0:
        args.workers = DEFAULT_MAX_WORKERS
    # Create crawler, a MyCrawler object
    crawler = MyCrawler(args.seeds, args.workers)
    # Start crawling
    crawler.crawl(args.count)


