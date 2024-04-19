@echo off
title "KYUCSA WEB SERVER START"
:: Replace this with the path to your virtual environment
cd env
set env_path=Scripts

:: Activate the virtual environment
call %env_path%\activate

:: Change directory to your Django app
cd ../

echo Trying to Start WebServer
:: Start the Django development server
start /min "KYUCSA WEBSITE" python manage.py runserver

:: Wait for a moment to ensure the server has started
timeout /nobreak /t 5

echo Waiting for 5 seconds to the server.
cls
echo Press any key to Launch Browser
pause
:: Open the default browser
start http://127.0.0.1:8000/
cls