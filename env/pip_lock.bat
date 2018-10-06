@echo off

(
    Scripts\activate
    pip freeze
    pip freeze > requirments.txt
    deactivate
)