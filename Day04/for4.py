'''
@Project ：PythonStudy 
@File    ：for4.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/22 21:15 
@description : 九九乘法表
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()