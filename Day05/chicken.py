'''
@Project ：PythonStudy 
@File    ：chicken.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/23 14:47 
@description : 《百钱百鸡》问题
'''
for x in range(0, 20):  #最多20只公鸡
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))