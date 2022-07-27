def doTest(len):
    print("begin...")
    i = 0
    while i < len:
        yield i
        print("yield:", i)
        i += 1
    print("end...")


x = doTest(5)
print(next(x))
print(next(x))
print(next(x))
