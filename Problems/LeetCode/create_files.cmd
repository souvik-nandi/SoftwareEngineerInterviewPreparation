@echo off
setlocal enabledelayedexpansion

rem Check if the file containing the list of filenames is provided as argument
if "%~1"=="" (
    echo Usage: %0 file_with_filenames
    exit /b 1
)

set "filename=%~1"

rem Check if the file exists
if not exist "%filename%" (
    echo Error: File "%filename%" not found.
    exit /b 1
)

rem Read filenames from the provided file and create files
for /f "usebackq tokens=*" %%i in ("%filename%") do (
    type nul > "%%i"
    echo File "%%i" created.
)

echo Files creation completed.
