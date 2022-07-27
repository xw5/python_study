import requests
import time
import json
from requests import urllib3
urllib3.disable_warnings()
url = 'https://ygjy.ismartwork.cn/ecs/mapp/restful/training/getPracticeTopicList'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) YGHome/4.7.0 Chrome/89.0.4389.82 Electron/12.0.1 Safari/537.36',
    'Cookie': 'ecpDataContext.tokenId=3d4462c931c64729848a12ce3b9c2985',
    'ecs_token': '3d4462c931c64729848a12ce3b9c2985',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'pageid': 'OnlineExerciseMainPage_orderPracticePage:YeE0kpIWRw1BT6JBPA94Bto4KcySpMbe',
    'Referer': 'https://ygjy.ismartwork.cn/ecs/mapp/manage/pc/microLearning/index.html'
}

totalPageNo = 0
resultConfig = []


def request_by_page(pageNo):
    params = {
        'pageNo': pageNo,
        'pageSize': 100,
        'categoryId': '0e9b6e3a970047eea9fb5b46d468655d',
        'trainingType': 1
    }
    res = requests.get(url=url, params=params, headers=headers, verify=False)

    code = res.status_code

    print(code)

    # 把响应数据存入变量中
    if code == 200:
        print('请求成功')
        result = res.json()
        print(result['body'])
        resultConfig.append(result['body'])

# 把存储数据写入到文件中
def write_file():
    with open('./研发质量能力认证练习New.js', 'w', encoding='utf8') as fp:
        fp.write(json.dumps(resultConfig, indent=4, ensure_ascii=False))


while totalPageNo < 20:
    request_by_page(totalPageNo)
    totalPageNo = totalPageNo + 1
    time.sleep(5)

write_file()
