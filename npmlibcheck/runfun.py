# coding=utf-8
import json
import xlwings as xw

# 开源协议
# 仓库主页
def otherInput(proPath, sht, dd, index, keys):
    try:
        with open('{}/node_modules/{}/package.json'.format(proPath, dd), "r", encoding='utf-8') as f:
            row_data_pkjson = json.load(f)
            for i, item in enumerate(keys):
                sht[index, i].value = row_data_pkjson.get(item, '未知')
    except:
        sht[index, 1].value = '访问出错'

def statisticsAction(proPath, outPath, keys, progressBack, uiName):
    # 读取文件数据
    with open(f'{proPath}/package.json', "r", encoding='utf-8') as f:
        row_data = json.load(f)
    proName = proPath.split('/')[-1]
    app = xw.App(visible=True, add_book=False)  # 启动Excel程序
    workbook = app.books.add()  # 新建工作簿
    workbook.save(f'{outPath}/{proName}.xlsx')  # 保存工作簿
    workbook.close()  # 关闭工作簿
    app.quit()
    wb = xw.Book(f'{outPath}/{proName}.xlsx')
    sht = wb.sheets['Sheet1']
    index = 0
    total = len(row_data['devDependencies']) + len(row_data['dependencies'])
    progress = str(index / total * 100) + '%'
    # 读取每一条json数据
    for d in row_data:
        if d == 'devDependencies':
            for dd in row_data[d]:
                sht[index, 0].value = dd
                otherInput(proPath, sht, dd, index, keys)
                index = index + 1
                progress = str(index / total * 100) + '%'
                progressBack(uiName, progress)
        if d == 'dependencies':
            for dd in row_data[d]:
                sht[index, 0].value = dd
                otherInput(proPath, sht, dd, index, keys)
                index = index + 1
                progress = str(index / total * 100) + '%'
                progressBack(uiName, progress)

