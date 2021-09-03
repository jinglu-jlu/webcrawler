# Crawler
## Overview
Crawler is a simple multi-threaded web crawler which fetches URLs uisng BFS and outputs crawl results to console and log as the crawl proceeds. It starts with a given set of URLs, and keeps crawling until user enter CTRL-C or the number of crawled pages reaches the specified count. This implementation only take URLs from \<a href\> tags and only processes absolute links.

## Usage
Crawler accepts one positional argument, and two optional arguments. Run '***python crawler.py -h***' for details.

![image](https://user-images.githubusercontent.com/17411814/131932976-09a155de-d341-4418-9aa8-ea1b9e73c80a.png)

### Examples
* Run crawler with a single seed url and 20 worker threads. Stop after crawling 100 urls.

***python spider.py https&#65279;://source.android.com/setup/start/build-numbers***

* Run crawler with a single seed url and 10 worker threads. Stop after crawling 150 urls.

***python spider.py https&#65279;://source.android.com/setup/start/build-numbers -c 150 -w 10***

* Run crawler with two seed urls and 30 work threads. Stop after crawling 300 urls.

***python spider.py https&#65279;://source.android.com/setup/start/build-numbers https&#65279;://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_processors -c 300 -w 30***

### To stop crawler before it completes
Press Ctrl+C

## Output
Crawler outputs to both stdout and log. The output is formated as below

![image](https://user-images.githubusercontent.com/17411814/131935585-863f01c7-200b-48b4-82f7-864e212f2cb2.png)

### Example

![image](https://user-images.githubusercontent.com/17411814/131935379-bcba9d9d-ad27-459a-987a-ecb3be30f781.png)

## Install and Build
### For Windows
1. Download crawler.py and buildcrawler.bat
2. Run buildcrawler.bat to setup virtualenv to run crawler: buildcrawler.bat
### For Other Platforms
TBD
## Run
### For Windows
1. Run activatecrawler.bat to activate virtualenv (if not activate yet)
2. Run crawler - see examples in Usage

### For other platforms
TBD




