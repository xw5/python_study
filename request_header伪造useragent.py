import requests

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360SE/12.2.1813.0'
}
res = requests.get(url=url, headers=headers, verify=False)

code = res.status_code

print(code)

# 响应成功把响应的内容写入文件中
if code == 200:
    with open('./test.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)