# Crawler
## Overview
Crawler is a simple web crawler which fetches URLs uisng BFS and outputs crawl results to console and file as the crawl proceeds 
## Install 
### For Windows
1. Download crawler.py and buildcrawler.bat
2. Run buildcrawler.bat to setup virtualenv to run crawler: buildcrawler.bat
### For other platforms
TBD
## Run
### For Windows
1. If the virtualenv is not activated yet, run activatecrawler.bat: *activatecrawler.bat*
2. Run crawler
The program accepts one positional argument, and two optional arguments. Run 'python crawler.py -h' for details
*python crawler.py -h*
usage: crawler.py [-h] [-c COUNT] [-w WORKERS] seed url [seed url ...]

positional arguments:
  seed url              seed urls (separated by space)

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of pages to crawl
  -w WORKERS, --workers WORKERS
                        number of worker threads

Examples
*python crawler.py https://source.android.com/setup/start/build-numbers*
*python crawler.py https://source.android.com/setup/start/build-numbers -c 100 -w -20*
*python crawler.py https://source.android.com/setup/start/build-numbers https://www.yahoo.com
### For other platforms
TBD




