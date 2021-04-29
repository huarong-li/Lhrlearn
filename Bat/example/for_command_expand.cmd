@echo off 

@rem 使用help for命令查看for命令变量扩展

setlocal enabledelayedexpansion
cd %~dp0..
set pwd="%cd%"
echo %pwd%
cd %~dp0
for /R "%pwd%" %%i in (*) do ( 
    set filename=%%~nxi 
    echo !filename!
    echo %%i
    echo %%~xi
) 
endlocal

pause

