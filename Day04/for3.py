'''
@Project ：PythonStudy 
@File    ：for3.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/22 21:08 
@description : 用for循环实现1~100之间的偶数求和
'''
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)