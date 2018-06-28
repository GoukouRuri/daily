# coding=utf-8

# 输入月份(数字),得到对应月份的英文缩写

month_number = input("请输入月份（数字1-12）:")

pos = int(month_number) - 1
month_list = "JanFebMarAprMayJunJulAugSepOctNovDec"

month_result = month_list[pos*3:(pos+1) * 3]
print("您输入的月份的英文缩写为: %s" %(month_result)) 












