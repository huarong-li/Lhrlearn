@rem 删除文件中读取文件路径，然后删除文件

@echo off

@rem /f 强制删除只读文件 /s 从所有子目录删除指定文件 /q 安静模式，删除时不要求确认

@rem 创建一个随机名字txt文件
set "filename=1"
call:generate_guid filename
@rem echo file: %filename%

@rem 创建空文件，需要使用随便字符+空格 2>nul > filename.txt 或者 type nul > filename.txt 创建
2  2>nul > %filename%.txt

@rem 创建10个随机名字txt文件
setlocal enabledelayedexpansion
set "filename=1"
for /l %%i in (1,1,10) do (
    call:generate_guid filename
    @rem echo %%i !filename!
    type nul > !filename!.txt
)
endlocal

dir /b > test.txt

@rem 获取文件中随机一行文本
setlocal enabledelayedexpansion
for /f "tokens=*" %%i in (test.txt) do (set /a h+=1 & set r!h!=%%i)
set /a s=%random%%%%h%+1
echo !r%s%!
endlocal

setlocal enabledelayedexpansion
for /f "tokens=*" %%i in (test.txt) do (
    set /a h+=1 & set r!h!=%%i
    @rem echo %%i
    @rem echo %%~xi
    if exist %%i (
        if "%%~xi" == ".txt" del %%i
    )
)
endlocal

pause

goto:eof

:generate_guid     -- generate guid string.
::                 -- %~1: return variable reference
setlocal enabledelayedexpansion
for %%i in ("0=A" "1=B" "2=C" "3=D" "4=E" "5=F")do set "x1%%~i"

set "guid="
for /l %%i in (1,1,32)do (
set/a "n=!random!&15"
if !n! gtr 9 call set "n=%%x!n!%%"
set "guid=!guid!!n!")
set "guid=%guid:~,8%-%guid:~8,4%-%guid:~12,4%-%guid:~16,4%-%guid:~-12%"

@rem echo %guid%

( endlocal & rem -- RETURN VALUES
   if "%~1" neq "" set %~1=%guid%
)
goto:eof
