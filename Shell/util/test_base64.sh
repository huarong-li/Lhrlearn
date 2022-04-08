#! /bin/bash

# 使用base64进行加解密字符串或者文件
echo PHY91 | base64

echo UEhZOTEK | base64 -d

echo "12345" | base64 | base64 -d


# 版本自增
version=1.0.02
echo $version | awk -F'.' '{print($1"."$2"."($3+1));}' 

# 生成随机字符串
echo $RANDOM | md5sum | cut -c 1-8
openssl rand -base64 8

# 生成随机数字
echo $RANDOM | cksum | cut -c 1-8
openssl rand -base64 8 | cksum | cut -c 1-8
date +%N | cut -c 1-8

