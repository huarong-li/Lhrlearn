#! /bin/bash

# $1 file path
# $2 sec
# $3 key
function get_sec_value(){
    local file_name="${1}" # cfg文件
    local sec_name="${2}" # 一个key-vaLue按名
    local key_name="${3}" # 一个key-vaLue块中的key
    local line_number=$(cat ${file_name} | grep -n "^[ ]*\[[ ]*${sec_name}[ ]*\]" | sed -n '1p' | awk -F ':' '{print $1}')
    # echo line_number=$line_number
    if [ "x${line_number}" = "x" ];then
        return 1
    fi
    # 获取目标key-vaLue块.并输出到临时文件中
    local temp_file="$(dirname ${file_name})/get_sec_value.$(date '+%Y%m%d%H%M%S')"
    awk -F '#' '{print $1}' ${file_name} | sed '/^[ ]*$/d' | sed -n "/^[ ]*\[[ ]*${sec_name}[ ]*\]/,/^[ ]*\[.*\]/p" | sed '/^[ ]*\[.*\]/d' > ${temp_file}
    # 若key_name不为空,则查找输出对应的值
    if [ "x${key_name}" != "x" ];then
        if [ "x$(cat ${temp_file} | grep "^[ ]*${key_name}[ ]*=.*" | sed -n '1p')" != "x" ];then
            echo $(cat ${temp_file} | grep "^[ ]*${key_name}[ ]*=.*" | sed -n '1p' | awk -F '=' '{print $2}')
            rm -f ${temp_file}
            return 0
        else
            rm -f ${temp_file}
            return 1
        fi
    fi

    # 若key_name为空,剩短目标块中的所有行输出到一个数组中
    local count=0
    unset RETURN
    while read line
    do
        RETURN[${count}]=${line}
        ((count+=1))
    done < ${temp_file}

    rm -f ${temp_file}
    return 0
}

echo username=$(get_sec_value ./config.cfg c c) \$\?=$?
echo IP=$(get_sec_value ./config.cfg server IP) \$\?=$?
echo DNS=$(get_sec_value ./config.cfg server IP) \$\?=$?
echo MASK=$(get_sec_value ./config.cfg server MASK) \$\?=$?

