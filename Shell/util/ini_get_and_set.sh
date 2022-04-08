#! /bin/bash

# dealIni.sh iniFile section option
# read
# param : iniFile section option    return value --- a str    use: ${iniValue}
# param : iniFile section           return options (element: option = value) --- a str[]   use: arr_length=${#iniOptions[*]}}  element=${iniOptions[0]}
# param : iniFile                   returm sections (element: section ) --- a str[]   use: arr_length=${#iniSections[*]}}  element=${iniSections[0]}
# write
#param : -w iniFile section option value  add new element&#xff1a;section option    result:if not --->creat ,have--->update,exist--->do nothing
#option ,value can not be null

# params
iniFile=$1
section=$2
option=$3
# sun
mode="iniR"
echo $@ | grep "\-w" >/dev/null&&mode="iniW"
if [ "$#" = "5" ]&&[ "$mode" = "iniW" ];then
    iniFile=$2
    section=$3
    option=$4
    value=$5
    # echo $iniFile $section $option $value
fi
# resullt
iniValue='default'
iniOptions=()
iniSections=()

function checkFile()
{
    if [ "${1}" = ""  ] || [ ! -f ${1} ];then
        echo "[error]:file --${1}-- not exist!"
    fi
}

function readInIfile()
{
    local iniFile=$1
    local section=$2
    local option=$3
    local iniValue='default'
    local iniOptions=()
    local iniSections=()
    if [ "${section}" = "" ];then
        # 通过如下两条命令可以解析成一个数组
        allSections=$(awk -F '[][]' '/\[.*]/{print $2}' ${iniFile})
        iniSections=(${allSections// /})
        echo "[info]:iniSections size:-${#iniSections[@]}- eles:-${iniSections[@]}- "
    elif [ "${section}" != "" ] && [ "${option}" = "" ];then
        # 判断section是否存在
        allSections=$(awk -F '[][]' '/\[.*]/{print $2}' ${iniFile})
        echo $allSections|grep ${section}
        if [ "$?" = "1" ];then
            echo "[error]:section --${section}-- not exist!"
            return 0
        fi
        # 正式获取options
        # a=(获取匹配到的section之后部分|去除第一行|去除空行|去除每一行行首行尾空格|将行内空格变为@G@(后面分割时为数组时&#xff0c;空格会导致误拆))
        a=$(awk "/\[${section}\]/{a=1}a==1"  ${iniFile}|sed -e '1d' -e '/^$/d'  -e 's/[ \t]*$//g' -e 's/^[ \t]*//g' -e 's/[ ]/@G@/g' -e '/\[/,$d' )
        b=(${a})
        for i in ${b[@]};do
            # 剔除非法字符&#xff0c;转换@G@为空格并添加到数组尾
            if [ -n "${i}" ]||[ "${i}" i!= "@G@" ];then
                iniOptions[${#iniOptions[@]}]=${i//@G@/ }
            fi
        done
        echo "[info]:iniOptions size:-${#iniOptions[@]}- eles:-${iniOptions[@]}-"
    elif [ "${section}" != "" ] && [ "${option}" != "" ];then

        # iniValue=`awk -F '=' '/\['${section}'\]/{a=1}a==1&&$1~/'${option}'/{print $2;exit}' $iniFile|sed -e 's/^[ \t]*//g' -e 's/[ \t]*$//g'`
        iniValue=`awk -F '=' "/\[${section}\]/{a=1}a==1" ${iniFile}|sed -e '1d' -e '/^$/d' -e '/^\[.*\]/,$d' -e "/^${option}.*=.*/!d" -e "s/^${option}.*= *//"`
        echo "[info]:iniValue value:-${iniValue}-"
    fi
}

function writeInifile()
{
    local iniFile=$1
    local section=$2
    local option=$3
    local value=$4
    local iniValue='default'
    local iniOptions=()
    local iniSections=()
    # 检查文件
    checkFile ${iniFile}
    allSections=$(awk -F '[][]' '/\[.*]/{print $2}' ${iniFile})
    iniSections=(${allSections// /})
    # 判断是否要新建section
    sectionFlag="0"
    for temp in ${iniSections[@]};do
        if [ "${temp}" = "${section}" ];then
            sectionFlag="1"
            break
        fi
    done

    if [ "$sectionFlag" = "0" ];then
        echo "[${section}]" >>${iniFile}
    fi
    # 加入或更新value
    awk "/\[${section}\]/{a=1}a==1" ${iniFile}|sed -e '1d' -e '/^$/d'  -e 's/[ \t]*$//g' -e 's/^[ \t]*//g' -e '/\[/,$d'|grep "${option}.\?=">/dev/null
    if [ "$?" = "0" ];then
        # 更新
        # 找到制定section行号码
        sectionNum=$(sed -n -e "/\[${section}\]/=" ${iniFile})
        sed -i "${sectionNum},/^\[.*\]/s/\(${option}.\?=\).*/\1 ${value}/g" ${iniFile}
        echo "[success] update [$iniFile][$section][$option][$value]"
    else
        # 新增
        # echo sed -i "/^\[${section}\]/a\\${option}=${value}" ${iniFile}
        echo $(sed "/^\[${section}\]/a\\${option} = ${value}" ${iniFile})
        sectionNum=$(sed -n -e "/\[${section}\]/=" ${iniFile})
        sectionNum1=`expr $sectionNum + 1`
        sectionNum2=$(sed -n -e "$(expr $sectionNum + 1),/\[.*\]/=" ${iniFile} | tail -n1)
        echo sectionNum1=$sectionNum1,$sectionNum2
        # sed -i "/^\[${section}\]/a\\${option} = ${value}" ${iniFile}
        sed -i "${sectionNum2} i\\${option} = ${value}\n" ${iniFile}
        echo "[success] add [$iniFile][$section][$option][$value]"
    fi
}

# main
# if [ "${mode}" = "iniR" ];then
#     checkFile
#     readInIfile
# elif [ "${mode}" = "iniW" ];then
#     writeInifile
# fi

# for test
echo $(awk -F '[][]' '/\[.*]/{print $2}' ./config.cfg)
echo $(awk -F '=' '/server/{a=1}a==1&&$1~/'IP'/{print $2;exit}' ./config.cfg)
echo $(awk -F '=' '/b/{a=1}a==1&&$1~/'IP'/{print $2;exit}' ./config.cfg)

echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg)
echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg | sed -e '1d')
echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg | sed -e '1d' -e '/^$/d')
echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg | sed -e '1d' -e '/^$/d' -e '/^\[.*\]/,$d')
echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg | sed -e '1d' -e '/^$/d' -e '/^\[.*\]/,$d' -e "/^IP *=.*/!d")
echo $(awk -F '=' '/\[b\]/{a=1}a==1' ./config.cfg | sed -e '1d' -e '/^$/d' -e '/^\[.*\]/,$d' -e "/^IP *=.*/!d" -e "s/^IP *=//")

readInIfile ./config.cfg "server" "IP"
readInIfile ./config.cfg "b" "IP"
readInIfile ./config.cfg "server" "DNS"
readInIfile ./config.cfg "server" "DNS1"

readInIfile ./config.cfg "server" "MASK"
writeInifile ./config.cfg "server" "MASK" "255.255.255.0"
readInIfile ./config.cfg "server" "MASK"
