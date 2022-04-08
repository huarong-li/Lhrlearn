#!/bin/bash
PRICE=$(expr $RANDOM % 1000)
t=0
echo “商品价格为0-999之间,猜猜看”
while true
do
read -p "请输入您猜测的价格: " I
        let t++
if [ $I -eq $PRICE ]
  then
        echo "恭喜你猜对了，实际价格是 $PRICE"
        echo "您总共猜测了 $t 次"
         exit 0
elif [ $I -gt $PRICE ]
        then
        echo "太高了"
        else
        echo "太低了"
fi
done
