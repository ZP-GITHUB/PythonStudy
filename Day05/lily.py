'''
@Project ：PythonStudy 
@File    ：lily.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/23 14:32 
@description : 找出所有水仙花数
'''
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)