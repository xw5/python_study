from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}

# 创建一个cookiejar
cookiejar = CookieJar()
# 使用cookiejar创建HTTPCookieProcessor
handler = request.HTTPCookieProcessor(cookiejar)
# 使用handler创建一个opener
opener = request.build_opener(handler)

# 使用opener发起登录请求
login_url = 'http://www.renren.com/PLogin.do'

data = {
    'email': '970138074@qq.com',
    'password': 'pythonspider'
}

req = request.Request(login_url, parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(req)

# 访问目录页
target_url = 'http://www.renren.com/880151247/profile'
target_req = request.Request(target_url, headers=headers)
result = opener.open(target_req)
print(result.read().decode('utf-8'))