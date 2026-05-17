@echo off

cd /d "%~dp0"

REM Create Reports folder if not exists
if not exist Reports mkdir Reports

REM Create Screenshots folder if not exists
if not exist Screenshots mkdir Screenshots

REM Delete old screenshots if present
if exist Screenshots\*.png del /q Screenshots\*.png

REM Delete old reports if present
if exist Reports\*.html del /q Reports\*.html

REM Run pytest
C:\Python314\python.exe -m pytest tests/test_searchAndApply.py -v --html=Reports/report.html --self-contained-html