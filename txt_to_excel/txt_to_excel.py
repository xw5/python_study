import re

pattern = re.compile(r'IDS_[\w\W]+"(?=\n)')

result = []
with open("test2.txt", "r", encoding='gbk') as f:  # 打开文件
    data = f.read()  # 读取文件
    it = re.finditer(pattern, data)
    for match in it:
        item_str = match.group()
        pattern_split = r'\s+'
        ite_str_list = re.split(pattern_split, item_str)
        # result.extend(ite_str_list)
        result.append(ite_str_list)
print(result)
