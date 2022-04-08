#! /bin/bash

WIN_ROOT="$(command -v cygpath1 > /dev/null && exec cygpath -Wu)"
echo WIN_ROOT: $WIN_ROOT

WIN_ROOT1="$(type cygpath > /dev/null 2>&1 && exec cygpath -Wu)"
echo WIN_ROOT1: $WIN_ROOT1

check_program_installed() {
    hash $1 > /dev/null 2>&1
    if [ "$?" != "0" ]; then
        echo "command $1 not found. is it installed?."
        return 1
    fi
    return 0
}

check_program_installed pwd
if [ $? -ne 0 ]; then
    echo pwd error.
fi
check_program_installed pwd1
if [ $? -ne 0 ]; then
    echo pwd1 error.
fi