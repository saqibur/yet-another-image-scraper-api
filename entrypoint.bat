@echo off
call venv\Scripts\activate
call python manage.py collectstatic --no-input
call python manage.py migrate --no-input
