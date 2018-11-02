@echo off

(
    Scripts\activate
    pip freeze
    pip freeze > requirements.txt
    deactivate
)