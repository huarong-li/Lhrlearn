@rem 删除文件中读取文件路径，然后删除文件

@echo off

@rem /f 强制删除只读文件 /s 从所有子目录删除指定文件 /q 安静模式，删除时不要求确认


for %%i in ("0=A" "1=B" "2=C" "3=D" "4=E" "5=F")do set "x1%%~i"
setlocal enabledelayedexpansion
set "guid="
for /l %%i in (1,1,32)do (
set/a "n=!random!&15"
if !n! gtr 9 call set "n=%%x!n!%%"
set "guid=!guid!!n!")
set "guid=%guid:~,8%-%guid:~8,4%-%guid:~12,4%-%guid:~16,4%-%guid:~-12%"

echo %guid%

pause
