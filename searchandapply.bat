@echo off

cd /d "%~dp0"

if not exist Reports mkdir Reports

C:\Python314\python.exe -m pytest tests/test_searchAndApply.py -v --html=Reports/report.html --self-contained-html