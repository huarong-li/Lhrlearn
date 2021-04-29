@echo off
setlocal enabledelayedexpansion

set python_env=C:\Python27amd64;C:\Python27amd64\Scripts
set visualstudio_env=C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE

set PYTHON_PATH=C:\Python27amd64

echo %PATH% | find /i "%python_env%" >nul && echo python_env is exist || if ERRORLEVEL 1 set PATH=%python_env%;%PATH%
echo %PATH% | find /i "%visualstudio_env%" >nul && echo visualstudio_env is exist || if ERRORLEVEL 1 set PATH=%visualstudio_env%;%PATH%

swig -c++ -python -outdir foxit -o ./invoke/example_wrap.cxx .\example.i

rem if not exist .\win64_rel_python_shared (md .\win64_rel_python_shared)

rem cd .\win64_rel_python_shared
rem cmake .. -DSDK_CONFIG=rel -DWINDOWS_COMPILE="Visual Studio 15" -DARCH=x64 -G "Visual Studio 15 Win64" -DENABLE_OCR=false

rem devenv FSDK.sln /build "Release|x64"  /project "ALL_BUILD.vcxproj"
rem cd ..

set vs_vc_env=C:\Users\HRong\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0
set VS90COMNTOOLS=%vs_vc_env%

set VCINSTALLDIR=%VS90COMNTOOLS%\VC\
set WindowsSdkDir=%VS90COMNTOOLS%\WinSDK\
rem if not exist "%VCINSTALLDIR%Bin\amd64\cl.exe" goto missing
set PATH=%VCINSTALLDIR%Bin\amd64;%WindowsSdkDir%Bin\x64;%WindowsSdkDir%Bin;%PATH%
set INCLUDE=%VCINSTALLDIR%Include;%WindowsSdkDir%Include;%INCLUDE%
set LIB=%VCINSTALLDIR%Lib\amd64;%WindowsSdkDir%Lib\x64;%LIB%
set LIBPATH=%VCINSTALLDIR%Lib\amd64;%WindowsSdkDir%Lib\x64;%LIBPATH%

SET DISTUTILS_USE_SDK=1
SET MSSdk=1

python .\setup.py build

python .\setup.py install

pause
