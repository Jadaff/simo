# coding: utf-8
# @Date : 2018/4/23


import requests

url = "http://fanyi.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
print(requests.get(url, headers=headers).cookies)
# 接口的参数
# params = {
#     "from": "en",
#     "to": "zh",
#     "query": "test"
# }
#
# r = requests.post(url, params=params)
#
# # 打印返回结果
# print(r.cookies)
# print(r.text)
