# https://api.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&next_openid=NEXT_OPENID

import requests
import json


def get_openid(self):
    '''
    获取要推送用户的openid
    :return:
    '''
    next_openid = ''  # 第一个拉取的OPENID，不填默认从头开始拉取 ，一次只能获取10000条
    url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
        self.get_token(), next_openid)
    ans = requests.get(url_openid)
    openid = json.loads(ans.content)['data']['openid']
    return openid
