#!/usr/bin/python
# -*- coding:utf-8 -*-

import xlrd

def xlsxReadFunc():
    try:
        #若输入的excel不存在，则打开excel报错
        book = xlrd.open_workbook('test.xlsx')
    except Exception as e:
         print('error msg:', e)
    else:
        sheet = book.sheet_by_index(0)
        cols = sheet.ncols
        #获取excel的总行数
        rows = sheet.nrows
        stu_list = []
        #循环读取每行数据，第0行是表头信息，所以从第1行读取数据
        for row in range(1, rows):
            stu = {}
            for col in range(0, cols):
                stu[col] = sheet.cell(row, col).value
            
            # 获取第row行的第0列所有数据
            # id = sheet.cell(row, 0).value
            # name = sheet.cell(row, 1).value
            # sex = sheet.cell(row, 2).value
            # 将id、name、sex添加到字典，若元素不存在则新增，否则是更新操作
            # stu['id'] = id
            # stu['name'] = name
            # stu['sex'] = sex

            stu_list.append(stu)
        print(stu_list)



if __name__ == "__main__":
    xlsxReadFunc()

    print('xls End')