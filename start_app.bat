@echo off
cd /d "C:\path\to\your\app\Users\axie\Journal"
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
pause
