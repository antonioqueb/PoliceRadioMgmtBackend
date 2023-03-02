@echo off

:menu
echo ============================================
echo =                  MENU                     =
echo ============================================
echo.
echo 1. python manage.py runserver (alias: server)
echo 2. python manage.py makemigrations (alias: makemigrations)
echo 3. python manage.py migrate (alias: migrate)
echo 4. python manage.py tests (alias: test)
echo 5. python manage.py inspectdb (alias: inspectdb)
set /p choice=Enter choice: 
goto option%choice%

:option1
python manage.py runserver
goto menu

:option2
python manage.py makemigrations
goto menu

:option3
python manage.py migrate
goto menu

:option4
python manage.py test
goto menu

:option5
python manage.py inspectdb > models.py
goto menu
