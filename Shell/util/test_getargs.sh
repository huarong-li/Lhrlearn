#! /bin/bash

echo \$\#=$#
echo \$\?=$?

if [[ $# = 0 ]]
then
echo need input PARAM!
exit
fi

echo \$0 $0
echo \$1 $1
echo \$\* $*
echo \$\@ $@

for arg in "$@"
do
echo $arg
done

