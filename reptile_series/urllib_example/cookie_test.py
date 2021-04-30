from urllib import request

url = 'https://view.ygsoft.com/_Home/R2012/index.aspx'

headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Cookie': 'ASP.NET_SessionId=itsowh3nxateiej0l3vqp5i1; CommunityServer-LastVisitUpdated-13127=; CommunityServer-UserCookie13127=lv=Mon, 31 Aug 2020 11:28:05 GMT&mra=Mon, 14 Sep 2020 13:57:26 GMT; UM_distinctid=175b1f4eb1d571-0b80f340a65c15-3e604902-1fa400-175b1f4eb1e959; isg=BN_f5hUQ_FwTEPi_cgghZDU0bjNjcDPvfX2IEHEt9Q6SAPqCeRdKNCcRxpB-mAte; Hm_lvt_bcba971a032a2c9b95dfcef8accf90d5=1611020330; Hm_lpvt_bcba971a032a2c9b95dfcef8accf90d5=1611020330; Hm_lvt_1dfd79c3c8bc90d15715933bf3281913=1611020330; Hm_lpvt_1dfd79c3c8bc90d15715933bf3281913=1611020330; FailLoginCnt=; uid=TVya0kIjjgE401qsthe4zQ==; UserInfoR2012=uName=xiewu@ygsoft.com; .ASPXFORMSAUTH=E8451A8A1CC0A9AE21E2EB9B8F6AE39056EDD7F36D77A0C6646BC8ADE668B48485C9E01C2958A0C718818AF1261DC0B27D6C0DB79F91F7402E71A9DF4DDC754EC13047AAC24FFFE0A1617C3D13C7B6D09F40FF564B6510C5720C20D21ECA2FF75665B821800D90214E74CF3AC99907D502A82D5040298989F14DC49BFD178EE8F1281622'
}

rep = request.Request(url=url, headers=headers)
result = request.urlopen(rep)
# print(result.read())

with open('ygsoftehome.html', 'w', encoding='utf-8') as fb:
    fb.write(result.read().decode('gbk'))