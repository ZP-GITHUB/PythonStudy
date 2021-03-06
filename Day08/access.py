'''
@Project ：PythonStudy 
@File    ：access.py
@IDE     ：PyCharm 
@Author  ：zhangpeng
@Date    ：2021/7/28 22:41 
@description : 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，
在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。
'''
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()