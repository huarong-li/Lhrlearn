#! /bin/bash

# $1 key
# $2 file path
function get_key_value(){
    info_line=`sed -n "/^$1/p" $2`
    if [[ -z $info_line ]];then
        # echo "$1 is null"
        return 1
    fi

    local key="$(echo "$1" | sed 's|[&]|\\&|g')"
    local current=$(sed -ne "s/^\($key *= *\)\([^ ']*\)\(.*\)$/\2/p" $2)
    if [ -n "$current" ]; then
        echo $current
        # 移除value的quotes
        # echo $current | sed -e 's/^["]*//g' | sed -e 's/["]*$//g'
        return 0
    fi
    return 1
}

# $1 file path
# $2 key
# $3 value
function set_key_value(){
    if [ ! -f $1 ]; then
        echo "file $1 is not exist!"
        return 1
    fi
    local key=${2}
    local value=${3}
    if [ -n "$value" ]; then
        # echo $value
        local current=$(sed -ne "s/^\($key *= *\)\([^ ']*\)\(.*\)$/\2/p" $1)
        if [ -n "$current" ]; then
            # echo "setting $1 : $key = $value"
            value="$(echo "${value}" | sed 's|[&]|\\&|g')"
            sed -i "s|^[#]*[ ]*${key}\([ ]*\)=.*|${key} = ${value}|" ${1}
        else
            # echo "create $1 new: $key = $value"
            value="$(echo "${value}" | sed 's|[&]|\\&|g')"
            echo "${key} = ${value}" >> $1
        fi
    fi
}

username1=`get_key_value username1 ./userinfo.txt`
echo username1=$username1 \$\?=$?

username=`get_key_value username ./userinfo.txt`
echo username=$username \$\?=$?

len=`get_key_value len ./userinfo.txt`
echo len=$len \$\?=$?

log_path=`get_key_value test.log_path ./userinfo.txt`
echo log_path=$log_path \$\?=$?

set_key_value ./userinfo.txt "fsync" "off"
set_key_value ./userinfo.txt "fsync1" "off22333"
