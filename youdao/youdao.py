# -*- encoding: utf-8 -*-

import requests
from datetime import datetime
import random
import hashlib

ts = str(int(datetime.now().timestamp()*1000))
salt = ts + str(int(random.random() * 10))
signstr = "fanyideskweb" + "apple" + salt + "@6f#X3=cCuncYssPsuRUE"
md5 = hashlib.md5()
sign = md5.update(signstr.encode('utf-8'))
sign = str(md5.hexdigest())


data = {
    'i': 'apple',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': str(int(datetime.now().timestamp()*1000)),
    'bv': 'a973a95daa8518a82e41685ce156ae19',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '242',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1001503668@59.83.221.35; JSESSIONID=abcJaYihoxWeB8_0qSHUw; OUTFOX_SEARCH_USER_ID_NCOO=1214517318.8526077; ___rl__test__cookies=1561791578930',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

response = requests.post(url, data=data, headers=headers)
print(response.json())
