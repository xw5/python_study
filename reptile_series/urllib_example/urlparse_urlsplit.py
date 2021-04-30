from urllib import parse
url = 'http://www.baidu.com/s;id?wd=python'

result = parse.urlparse(url)
print(result)
print(result.scheme)
print(result.netloc)
print(result.path)
print(result.query)

# 比urlparse少params
resultsSplit = parse.urlsplit(url)
print(resultsSplit)