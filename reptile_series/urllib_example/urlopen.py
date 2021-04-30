from urllib import request
result = request.urlopen('http://www.baidu.com')

# print(result.read())
# print(result.read(100))
# print(result.getcode())
# print(result.readline())
print(result.readlines())