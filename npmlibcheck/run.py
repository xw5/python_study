# coding=utf-8
import json
import xlwings as xw

proName = 'cici_pc_electron'
proPath = 'D:/work/workspace'

# 读取文件数据
with open(f'{proPath}/{proName}/package.json', "r", encoding='utf-8') as f:
    row_data = json.load(f)

app = xw.App(visible=True,add_book=False)	#启动Excel程序
workbook = app.books.add()			#新建工作簿
workbook.save(f'./{proName}.xlsx')	#保存工作簿
workbook.close()					#关闭工作簿
app.quit()
wb = xw.Book(f'./{proName}.xlsx')
sht = wb.sheets['Sheet1']
index = 0

# 开源协议
# 仓库主页
def otherInput(dd):
    global index
    global sht
    try:
        with open('{}/{}/node_modules/{}/package.json'.format(proPath, proName, dd), "r", encoding='utf-8') as f:
            row_data_pkjson = json.load(f)
            sht[index, 2].value = row_data_pkjson.get('license', '未知')
            sht[index, 3].value = row_data_pkjson.get('homepage', '未知')
    except:
        sht[index, 2].value = '未知'

# 读取每一条json数据
for d in row_data:
    if d == 'devDependencies':
        for dd in row_data[d]:
            sht[index, 0].value = dd
            sht[index, 1].value = row_data[d][dd][1:]
            otherInput(dd)
            index = index + 1
    if d == 'dependencies':
        for dd in row_data[d]:
            sht[index, 0].value = dd
            sht[index, 1].value = row_data[d][dd][1:]
            otherInput(dd)
            index = index + 1


