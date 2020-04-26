#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 实现对 excel文件内容读取
import xlrd
# 实现对 excel文件的写入
import xlwt

ms = []
ra = []
rb = []

# 遍历读取excel, 目前示例只有一个 excel表 B1，所以只遍历一个即可, rang中为前包含后不包含
# for k in range(1, 4):
for k in range(1, 2):
  # 依次读取文件
  data = xlrd.open_workbook("./data/B" + str(k) + ".xlsx")
  # 读取工作表 Sheet1
  table_1 = data.sheet_by_name("Sheet1")
  # 读取工作表 Sheet2
  table_2 = data.sheet_by_name("Sheet2")
  # 获取每个工作表中的行数
  rs1 = table_1.nrows
  rs2 = table_2.nrows

  m = 99
  for i in range(1, rs1):
    # 读取 Sheet1中每一行第四列的值: 出发时间
    t14 = table_1.cell(i, 4).value

    # t12 = t14 - table_1.cell(i, 2).value
    # print t12
  #   for j in range(1, rs2):
  #     t22 = table_2.cell(j, 2).value
  #     if t22 - t14 >= 1 / 24:
  #       m1 = t12 + (t22 - t14) + (table_2.cell(j, 4).value - t22)
  #       if m > m1:
  #         m = m1
  #         r1 = i
  #         r2 = j
  # ms.append(m)
  # ra.append(r1)
  # rb.append(r2)

# ms0 = min(ms)
# ms1 = ms.index(ms0)
# print("从A地出发经B", ms1 + 1, "到达B地，最少耗时为：", ms0 * 24, "小时。具体行程请查看文件ZHXC.XLS。")
# data = xlrd.open_workbook("./data/B" + str(ms1 + 1) + ".xlsx")
# table_1 = data.sheet_by_name("Sheet1")
# table_2 = data.sheet_by_name("Sheet2")

# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('sheet 1')
# for l in range(5):
#   sheet.write(0, l, table_1.cell(0, l).value)
#   sheet.write(1, l, table_1.cell(ra[ms1], l).value)
#   sheet.write(2, l, table_2.cell(rb[ms1], l).value)
# wbk.save('./data/zjxc.xls')
