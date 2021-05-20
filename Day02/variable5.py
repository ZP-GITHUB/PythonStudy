'''
@Project ：PythonStudy 
@File    ：variable5.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/20 22:53 
@description : 比较运算符和逻辑运算符的使用
'''
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False