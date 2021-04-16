import requests
# from requests import urllib3
# urllib3.disable_warnings()

loginUrl = 'http://cxytiandi.com/login'
url = 'http://cxytiandi.com/user/info'
data = {
    'username': 'xiewu5550@163.com',
    'password':'52ae0b003a3a11055aef9833273ea2dcb3ef11d8b0ac897231b35a9b8edd7268e84599717e55ac7e5b7347907115a834151d49bf3afc666ee02e77c9840014747a016d2121c60237e7008aac997ba7f4e6a141cac0e816c956923b658757b127fab62c87d038b84fbb813228e601fbe1e0ab807d99ad33268381f784fffc5569'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360SE/12.2.1813.0'
}

# 如果要记录cookie信息的，就要调用前先session()
req = requests.session()

res = req.post(url=loginUrl, data=data)
code = res.status_code

print(code)


# 响应成功把响应的内容写入文件中
if code == 200:
    print('登录成功')
    result = req.get(url=url, verify=False)
    resultCode = result.status_code
    if resultCode == 200:
        with open('猿天地.html', 'w', encoding='utf-8') as fp:
            fp.write(result.text)