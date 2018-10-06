@echo off

(
    cd env
    if not exist installed (
        echo "Installing environment"
        install
        echo true > installed
    )

    cd ..\src
    if not exist installed (
        echo "Migration started"
        migrate
        echo true > installed
        echo "Migration finished"
    )
)
