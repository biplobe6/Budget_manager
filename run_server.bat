@echo off
cd src

(
	..\env\Scripts\activate
	..\env\Scripts\python manage.py runserver 0:8074
)