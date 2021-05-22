'''
@Project ：PythonStudy 
@File    ：for2.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/22 21:07 
@description : 用for循环实现1~100之间的偶数求和
'''
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)