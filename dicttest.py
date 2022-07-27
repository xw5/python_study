dict = {'url': 'http://www.5bug.wang', 'name': '吾八哥网', 'webtype': '技术分享站', 'websystem': 'wordpress'}
# 打印key为xxx的元素值 print(dict[xxx])
print(dict['url'])
# 修改或者添加key为xxx的元素值
dict['url'] = 'http://5bug.wang'
dict['QQ群'] = '643829693'
# 删除key为xxx的元素值
dict.pop('websystem')
# 打印字典的长度
print(len(dict))
# 打印出所有的键值数据
for k, v in dict.items():
    print('key: %s  value: %s' % (k, v))
# 合并两个字典并且以字符形式打印出来
dict1 = {}
dict1 = dict1.fromkeys(['id', 'num'], 0)
dict.update(dict1)
print(str(dict))
dict0 = dict.items()
print(dict0)
print(dict0[0])
