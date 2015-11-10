# -*- coding: utf-8 -*-
__author__ = "minghao.mamh@alibaba-inc.com"

import openpyxl


def demo1(source_excel):
    book = openpyxl.load_workbook(source_excel)
    # 打印出所有sheet的name
    print(book.get_sheet_names())
    sheet = book[book.get_sheet_names()[0]]
    # 显示总行数
    row_count = sheet.max_row
    print("row count:{0}".format(row_count))
    # 将数据行的第一列设置为编号
    for i in range(2, row_count+1):
        cell = sheet.cell(row=i, column=1)
        cell.value = str(i - 1)
    # 将修改保存为一个新的文件
    print("output file: output.xlxs")
    book.save("output.xlsx")


if __name__ == "__main__":
    demo1("input.xlsx")