import datetime
import re

str = '2022年7月25日星期一'

print(re.sub(r'\D', '', str))