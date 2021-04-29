
@echo off

echo bat Function example
echo =================================
echo ==========Func No paramter ======
echo =================================
echo before call myFuncNoPara
call:myFuncNoPara
echo after call myFuncNoPara
echo =================================
echo ===========Func has paramter=====
echo =================================
echo before call myFuncHasPara
call:myFuncHasPara 123 abc
echo after call myFuncHasPara
echo =================================
echo =======Func with return value====
echo =================================
set return=123
set returnPara=321
echo return:%return%
echo returnPara:%returnPara%
echo befora call myFuncReturnValue
call:myFuncReturnValue returnPara abc
echo after call myFuncReturnValue
echo return:%return%
echo returnPara:%returnPara%

pause
:myFuncNoPara
echo myFuncNoPara enter
echo myFuncNoPara First para:%1
echo myFuncNoPara Second para:%2
echo myFuncNoPara Third para:%3
echo myFuncNoPara exit
goto:eof

:myFuncHasPara
echo myFuncHasPara enter
echo myFuncHasPara First para:%1
echo myFuncHasPara Second para:%2
echo myFuncHasPara Third para:%3
echo myFuncHasPara exit
goto:eof

:myFuncReturnValue
echo myFuncReturnValue
echo myFuncReturnValue First para:%1
echo myFuncReturnValue Second para:%2
set "%~1=%2%"
set return=%2
goto:eof

