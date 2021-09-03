@echo off
REM Creat virtualenv
python -m venv crawler
REM Install required packages
crawler\Scripts\pip.exe install requests
crawler\Scripts\pip.exe install bs4
crawler\Scripts\pip.exe install lxml
REM Create activate.bat
echo "crawler\Scripts\activate.bat" > activatecrawler.bat
REM Activate virtualenv
crawler\Scripts\activate.bat