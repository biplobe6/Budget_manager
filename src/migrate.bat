@echo off

if not exist templates (
	mkdir templates
)

if not exist staticfiles (
	mkdir staticfiles
)


(
	..\env\Scripts\activate
	..\env\Scripts\python manage.py makemigrations
	pause
	..\env\Scripts\python manage.py migrate
	pause
)
