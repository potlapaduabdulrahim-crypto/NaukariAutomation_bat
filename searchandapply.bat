@echo off

cd /d "%~dp0"

if not exist Reports mkdir Reports

py -m pytest tests/test_searchAndApply.py -v --html=Reports/report.html --self-contained-html

start Reports\report.html

pause