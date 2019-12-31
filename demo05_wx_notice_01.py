import json

import requests # HTTP库


# 1. 获取access_token
# https请求方式: GET 
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

app_id = 'wx7f23641379450a28'
app_secret = '2bfecd48e13964d00b4a1b0bf26b0acb'
url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'

resp = requests.get(url).json()
access_token = resp.get('access_token')


# 2. 利用access_token发送微信的通知
# http请求方式: POST
# https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN

url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}'
opend_id = "oqtB6wXelAcohf9rasCA7VLHNk9c"
req_data = {
    "touser": opend_id,
    "msgtype":"text",
    "text":
    {
         "content":"黑马程序员, 有人闯入了你的家"
    }
}
requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))

