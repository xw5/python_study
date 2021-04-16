import requests

url = 'https://www.lmonkey.com/'

res = requests.get(url=url)

code = res.status_code

print(code)

# 响应成功把响应的内容写入文件中
if code == 200:
    with open('./test.html', 'w',encoding='utf-8') as fp:
        fp.write(res.text)