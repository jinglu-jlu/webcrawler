@echo off
REM Build virutalenv to run crawler
mkdir crawler
REM Create a virtualenv
python3 -m venv /path/to/new/virtual/environment
REM Activate virtualenv
crawler\Scripts\activate.bat
REM Install required packages
pip install requests
pip install bs4
pip install lxml
REM Create symbolic link to crawler\Scripts\activate.bat
mklink activatecrawler crawler\Scripts\activate.bat
