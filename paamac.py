# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd

global null
null = ''
global true
true = 'true'
global false
false = 'false'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'Content-Type': 'application/json',
    'Cookie': 'td_cookie=1467723492',
    'Host': 'gs.amac.org.cn',
    'Origin': 'http://gs.amac.org.cn',
    'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
           }

request_url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager'

df_all = pd.DataFrame(columns=['artificialPersonName', 'establishDate', 'fundCount', 'fundScale',
       'hasCreditTips', 'hasSpecialTips', 'id', 'inBlacklist',
       'managerHasProduct', 'managerName', 'officeAddress', 'officeCity',
       'officeCoordinate', 'officeProvince', 'paidInCapital',
       'primaryInvestType', 'regAdrAgg', 'regCoordinate', 'registerAddress',
       'registerCity', 'registerDate', 'registerNo', 'registerProvince',
       'subscribedCapital', 'url'])

for page in range(10):
    data = {
        'rand':0.54231961,
        'page':page,
        'size':20
    }

    res = requests.post(request_url,data=json.dumps(data),headers= headers)

    res = res.text
    res = eval(res)
    df = pd.DataFrame(res['content'])
    df_all = df_all.append(df,ignore_index=True)
    print('第{}页爬取已经完成'.format(page))
df_all.to_csv('df.csv',encoding='utf-8')
print(df_all)