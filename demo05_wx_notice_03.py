import json

import requests # HTTP库

# 把代码从面向过程变成面向函数
# 我们可以接受定义的复杂，但是不能接受调用的复杂
# 把代码从面向函数改成面向对象

# 1. 获取access_token
# https请求方式: GET 
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

class WxTools():
    
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
       
    def get_access_token(self):
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}'
        resp = requests.get(url).json()
        access_token = resp.get('access_token')
        return access_token


    def send_wx_customer_msg(self, opend_id, msg="有人闯入了你的家"):
        url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={self.get_access_token()}'
        req_data = {
            "touser": opend_id,
            "msgtype":"text",
            "text":
            {
                  "content": msg
            }
        }
        requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))
    

# 2. 利用access_token发送微信的通知
# http请求方式: POST
# https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN


if __name__ == "__main__":
    app_id = 'wx7f23641379450a28'
    app_secret = '2bfecd48e13964d00b4a1b0bf26b0acb'
    # access_token = get_access_token(app_id, app_secret)
    # send_wx_customer_msg(access_token, "oqtB6wXelAcohf9rasCA7VLHNk9c")
    wx_tools = WxTools('wx7f23641379450a28', '2bfecd48e13964d00b4a1b0bf26b0acb')
    wx_tools.send_wx_customer_msg("oqtB6wXelAcohf9rasCA7VLHNk9c")
