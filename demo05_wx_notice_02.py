import json

import requests # HTTP库

# 把代码从面向过程变成面向函数
# 我们可以接受定义的复杂，但是不能接受调用的复杂

# 1. 获取access_token
# https请求方式: GET 
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET


def get_access_token(app_id, app_secret):
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'
    resp = requests.get(url).json()
    access_token = resp.get('access_token')
    return access_token


# 2. 利用access_token发送微信的通知
# http请求方式: POST
# https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN

def send_wx_customer_msg(access_token, opend_id, msg="有人闯入了你的家"):
    url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}'
    req_data = {
        "touser": opend_id,
        "msgtype":"text",
        "text":
        {
              "content": msg
        }
    }
    requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))


if __name__ == "__main__":
    app_id = 'wx7f23641379450a28'
    app_secret = '2bfecd48e13964d00b4a1b0bf26b0acb'
    access_token = get_access_token(app_id, app_secret)
    send_wx_customer_msg(access_token, "oqtB6wXelAcohf9rasCA7VLHNk9c")
