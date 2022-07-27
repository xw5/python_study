class MyClass:
    id = 1
    name = "名称"
    __tag = "这是类的私有属性"

    def test(self):
        print(self.id)
        print(self.name)
        print(self.__tag)

    def __init__(self, id, name):
        self.id = id
        self.name = name


# 单继承的类ChildAClass
class ChildAClass(MyClass):
    def __init__(self):
        self.name = "ChildAClass"

    # 覆写父类方法
    def test(self):
        # 调用父类的test方法，也可以使用：super(ChildAClass, self).test()
        MyClass.test(self)
        print("调用testfunc")

    def funcA(self):
        print("测试funcA方法")


c = ChildAClass()
c.test()
c.funcA()
