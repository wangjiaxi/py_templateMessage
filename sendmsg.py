class WechatSendmes():

    def __init__(self, appid, appsecret, template_id, ):
        self.appid = appid
        self.secret = appsecret
        self.template_id = template_id

    def get_token(self):
        '''
        获取access_token
        '''
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
            self.appid, self.secret)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers).json()
        print(res)
        return res["access_token"]

    def get_openid(self):
        '''
        获取要推送用户的openid
        :return:
        '''
        next_openid = ''  # 第一个拉取的OPENID，不填默认从头开始拉取 ，一次只能获取10000条
        url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
            self.get_token(), next_openid)
        ans = requests.get(url_openid)
        # print(ans.json())
        openid = json.loads(ans.content)['data']['openid']
        return openid

    def get_user_info(self):
        '''
        获取要推送用户的各种信息(内测组)
        '''
        for index, openid in enumerate(self.get_openid()):
            url_info = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN".format(
                self.get_token(), self.get_openid()[index])
            info = requests.get(url_info).json()
            with open("data.json", "a", encoding="utf-8", newline="\n") as f:
                json.dump(info, f, ensure_ascii=False)
            print(index, "已写入")
            # print(info["openid"], info["tagid_list"])
            # return info["tagid_list"]

    def get_tags(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token={}".format(
            self.get_token())
        info = requests.get(url).json()
        print(info)

    def tag_users(self):
        url = "https://api.weixin.qq.com/cgi-bin/user/tag/get?access_token={}".format(
            self.get_token())
        info = requests.post(
            url, json={"tagid": 100,   "next_openid": ""}).json()
        # print(info)

    def sendmes(self):
        '''
        推送到微信公众号
        :return:
        '''
        # global microbit01_name, microbit01_cost
        # author, origin, content = self.get_shici()
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(
            self.get_token())
        headers = {"Content-type": "application/json"}
        for index, template_id in enumerate(self.get_openid()):
            print(self.get_openid()[index])
            body = {
                # "touser": "ovNli6ToAd2sELQXfF8Yo5YZLGfc",
                "touser": self.get_openid()[index],
                "template_id": self.template_id,
                "url": "http://121.43.145.115/",
                # "page": "index",
                "data": {
                    "thing01": {
                        "value": microbit01_name[index]
                    },
                    "thing02": {
                        "value": "microbit"
                    },
                    "time01": {
                        "value": "10:00~12:00"
                    },
                    "thing03": {
                        "value": microbit01_cost[index]
                    }
                }
            }
            res = requests.post(url, json=body, headers=headers)
            print('推送成功') if res.json()[
                'errmsg'] == 'ok' else print(f'用户{template_id}推送失败')

    def sendmes_test(self):
        '''
        推送到微信公众号
        :return:
        '''
        # global microbit01_name, microbit01_cost
        # author, origin, content = self.get_shici()
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(
            self.get_token())
        headers = {"Content-type": "application/json"}
        for index, template_id in enumerate(tag_100):
            print(index, tag_100[index])
            body = {
                # "touser": "ovNli6ToAd2sELQXfF8Yo5YZLGfc",
                "touser": tag_100[index],
                "template_id": self.template_id,
                "url": "http://121.43.145.115/",
                # "page": "index",
                "data": {
                    "thing8": {
                        "value": "microbit"
                    },
                    "time5": {
                        "value": "10:00~12:00"
                    },
                    "thing7": {
                        "value": microbit01_name[index]
                    },
                    "character_string13": {
                        "value": microbit01_cost[index]
                    }
                }
            }
            res = requests.post(url, json=body, headers=headers)
            print(res.json())
            print('推送成功') if res.json()[
                'errmsg'] == 'ok' else print(f'用户{template_id}推送失败')



    # =======================硬壳=========================
    # push = WechatSendmes("wx5dec27a463e492cc", "aacbf9d08d1e05452c73f5c7c0bb3bf0",
    #  "ccpIeeEK9STrcyHkhC7TOlovxaljz43hBOc9TjCogbs")
    # push.sendmes()

    # test = WechatSendmes("wx5dec27a463e492cc", "aacbf9d08d1e05452c73f5c7c0bb3bf0",
    #                      "AJK1CjrzHKcQVuogp_nx0cGjNyGvP4C3SYePWAlt-ps")
    # print(test.get_token())
    # print(test.get_openid())
    # print(test.get_user_info())
    # test.sendmes_test()
    # print(test.tag_users())
    # print(test.get_tags())

    # get_ip()
