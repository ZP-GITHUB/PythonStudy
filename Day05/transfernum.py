'''
@Project ：PythonStudy 
@File    ：transfernum.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/23 14:44 
@description : 正整数的反转
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)