from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
print(html)

result = html.xpath('//ul/li/a/@href')
print(result)

result = html.xpath('//div[@class="test"]//li/a/text()')
print(result)