'''
@Project ：PythonStudy 
@File    ：module3.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/5/24 22:37 
@description : 
'''
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
