from urllib import request
import time

url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())
time.sleep(2)


# 使用代理 测试失败
# 使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({'http': '114.231.45.61:9999'})
# 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 使用opener去发送一个请求
proxyResp = opener.open(url)
print(proxyResp.read())