from urllib import request
from urllib import parse

params = {"name": "张三","age":18}
result = parse.urlencode(params)
print(result)

result = parse.parse_qs(result)
print(result)