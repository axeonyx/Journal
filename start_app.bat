@echo off
cd /d "C:\path\to\your\app\Users\axie\Journal"
pip install -r requirements.txt
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
pause
