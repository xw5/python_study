from lxml import etree

text = '''
<ul>
<li><a href="/api/request/request">发起请求</a></li>
<li><a href="/api/request/network-file">上传、下载</a></li>
<li><a href="/api/request/websocket">WebSocket</a></li>
<li><a href="/api/request/socket-task">SocketTask</a></li>
<li><a href="/api/request/mDNS">mDNS</a></li>
<li><a href="/api/request/UDP">UDP 通信</a></li>
</ul>
'''

# 使用etree解析html字符串
html = etree.HTML(text)
print(html)

result = html.xpath('/html/body/ul/li/a/text()')
print(result)