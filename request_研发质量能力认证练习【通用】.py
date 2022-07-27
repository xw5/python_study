import requests
import time
import json
# from requests import urllib3
# urllib3.disable_warnings()
url = 'https://ygjy.ismartwork.cn/ecs/mapp/restful/training/getPracticeTopicList'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) YGHome/4.7.0 Chrome/89.0.4389.82 Electron/12.0.1 Safari/537.36',
    'Cookie': 'ecpDataContext.tokenId=6d919a6193814997950733983c599b51',
    'ecs_token': '6d919a6193814997950733983c599b51',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ygjy.ismartwork.cn/ecs/mapp/manage/pc/microLearning/index.html'
}
totalPageNo = 0
resultConfig = []


def request_by_page(pageNo):
    params = {
        'pageNo': pageNo,
        'pageSize': 100,
        'categoryId': '12c9d95f15814072869fd79cefbc4a2f',
        'trainingType': 1
    }
    res = requests.get(url=url, params=params, headers=headers, verify=False)

    code = res.status_code

    print(code)

    # 响应成功把响应的内容写入文件中
    if code == 200:
        print('请求成功')
        result = res.json()
        print(result['body'])
        resultConfig.append(result['body'])


def write_file():
    with open('./【通用】研发质量能力认证练习20210823.js', 'w', encoding='utf8') as fp:
        fp.write(json.dumps(resultConfig, indent=4, ensure_ascii=False))


while totalPageNo < 14:
    request_by_page(totalPageNo)
    totalPageNo = totalPageNo + 1
    time.sleep(5)

write_file()
