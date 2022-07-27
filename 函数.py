# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("加了星号 * 的参数会以元组(tuple)的形式导入 输出: ")
    print(arg1)
    print(vartuple, vartuple[0])


# 调用printinfo 函数
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("加了两个星号 ** 的参数会以字典的形式导入 输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

# 可写函数说明
test = 5
sum = lambda arg1, arg2: arg1 + arg2 + test

# 调用sum函数
print("使用 lambda 来创建匿名函数")
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


# 形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)
f(10, b=20, c=30, d=40, e=50, f=60)  # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)  # e 必须使用关键字参数的形式
