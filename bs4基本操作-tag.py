from bs4 import BeautifulSoup

text = '''
<h1>BeautifulSoup title</h1>
<ul>
<li class="li1"><a href="/api/request/request">发起请求</a></li>
<li id="li1"><a href="/api/request/network-file">上传、下载</a></li>
<li><a href="/api/request/websocket">WebSocket</a></li>
<li><a href="/api/request/socket-task">SocketTask</a></li>
<li><a href="/api/request/mDNS">mDNS</a></li>
<li><a href="/api/request/UDP">UDP 通信</a></li>
</ul>
'''

soup = BeautifulSoup(text, 'lxml')

# 1 通过tag
# h1 = soup.h1
# li = soup.li
# a = soup.a['href']
#
# print(h1)
# print(li)
# print(a)

# 2 fint find_all
# aone = soup.find('a')
# ase = soup.find_all('a')
# liid = soup.find(id='li1')
# liclass = soup.find_all(class_='li1')
# print(aone)
# print(ase)
# print(liid)
# print(liclass)

# 3 css选择器
cssh1 = soup.select('h1')
cssLiclass = soup.select('.li1')
cssLiid = soup.select('#li1')

print(cssh1)
print(cssLiclass)
print(cssLiid)