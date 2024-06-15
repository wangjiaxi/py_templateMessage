import json
import requests
import tkinter as tk
import re
import tkinter.messagebox

APPID = "wx5dec27a463e492cc"
APPSECRET = "aacbf9d08d1e05452c73f5c7c0bb3bf0"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
tags_id = []
tags_name = []

# 窗口
window = tk.Tk()
window.title("Engeeker硬壳编程模板消息推送 v1.0")
window.geometry("1000x800")


def get_ip():
    """
    自动获取本机IP地址，需要公众号管理员将IP地址设为白名单才能推送模板消息\n
    返回值：IP地址字符串
    """
    url = "http://myip.ipip.net"
    ip_info = requests.get(url, timeout=6).text  # 获取IP地址的详细信息
    ip = re.findall(r"\d+\.\d+\.\d+\.\d+", ip_info,
                    flags=0)  # 正则匹配xx.xx.xx.xx格式
    print("本机" + ip_info)
    return ip[0]  # 列表只有一个元素


def get_ip_again():
    """
    手动获取本机IP地址，先清空Entry，再获取IP，再插入Entry\n
    返回值：无
    """
    entry_ip.delete(0, "end")
    entry_ip.insert(0, get_ip())


# ======IP地址的获取和显示=====================================================
label_ip = tk.Label(window, text="IP地址自动获取：")
label_ip.grid(row=0, column=0, padx=(10, 0), pady=10)
entry_ip = tk.Entry(window, width=15,)
entry_ip.grid(row=0, column=1, pady=10)
entry_ip.insert(0, get_ip())
button_ip = tk.Button(window, text="点击手动获取IP地址", command=get_ip_again)
button_ip.grid(row=0, column=2, padx=(10, 0), pady=10)


def get_token():
    '''
    获取access_token
    '''
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
        APPID, APPSECRET)
    res_json = requests.get(url).json()
    print(res_json)
    return res_json["access_token"]


access_token = get_token()


def get_tags():
    url = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token={}".format(
        access_token)
    res_json = requests.get(url, headers=headers).json()
    print(res_json)
    return res_json["tags"]


# 获取标签id和标签名称存入列表
# tags = get_tags()
tags = "0"
# for index in range(len(tags)):
#     tags_id.append(tags[index]["id"])
#     tags_name.append(tags[index]["name"])


def insert_tags():
    """
    在Text中插入id和对应name
    """
    for id in tags_id:
        text_tag_id.insert("-1.-1", str(id)+"\n")
    for name in tags_name:
        text_tag_name.insert("-1.-1", str(name)+"\n")


# ======tag获取和显示=====================================================
button_get_tag = tk.Button(window, text="点击获取标签", command=insert_tags)
button_get_tag.grid(row=1, column=0, padx=(0, 0), pady=10)
text_tag_id = tk.Text(window, width=20, height=5,
                      relief="sunken", borderwidth=1)
text_tag_id.grid(row=1, column=1, padx=(10, 10), pady=10)
text_tag_name = tk.Text(window, width=20, height=5,
                        relief="sunken", borderwidth=1)
text_tag_name.grid(row=1, column=2, padx=(10, 10), pady=10)


# ======选择推送班级=====================================================
label_choose = tk.Label(window, text="请输入推送班级ID：")
label_choose.grid(row=2, column=0, padx=(10, 0))
entry_choose = tk.Entry(window, width=15)
entry_choose.grid(row=2, column=1, pady=10)


def get_openid():
    """
    获取标签下粉丝列表，解析后存入text
    """
    if entry_choose.get():
        tagid = int(entry_choose.get())
    url = "https://api.weixin.qq.com/cgi-bin/user/tag/get?access_token={}".format(
        access_token)
    res_json = requests.post(
        url, json={"tagid": tagid, "next_openid": ""}).json()
    res = res_json["data"]["openid"]  # List
    for openid in res:
        text_tag_openid.insert("-1.-1", openid+"\n")
    return res


# microbit01_name = ["小可爱1", "小可爱2", "小可爱3", "小可爱4"]
# microbit01_cost = [20, 20, 30, 40]
# tag_100 = ["oY8_lskpL-HJtY8OUgr4E0Qhp6gI",
#            "oY8_lslE7tPcmkWBYrDa8_3D62w0",
#            "oY8_lskM9xAcjJAh1_VzPvoe0gFk",
#            "oY8_lsp6veaZE_lfWD1gAIsUNZLU"]


# ======点击获取openid=====================================================
button_get_openid = tk.Button(window, text="点击获取openid", command=get_openid)
button_get_openid.grid(row=3, column=0, padx=(10, 0))
text_tag_openid = tk.Text(window, width=30, height=8,
                          relief="sunken", borderwidth=1)
text_tag_openid.grid(row=3, column=1, pady=10)


# ======模板id=====================================================
label_template_id = tk.Label(window, text="模板id：")
label_template_id.grid(row=4, column=0, padx=(10, 0))
entry_template_id = tk.Entry(window, width=40)
entry_template_id.grid(row=4, column=1, pady=10)

# ======模板参数设置=====================================================
label_template_title = tk.Label(window, text="模板参数设置：")
label_template_title.grid(row=5, column=0, padx=(10, 0))
# 4个label
label_template_p1 = tk.Label(window, text="参数1：")
label_template_p1.grid(row=5, column=1, padx=(10, 0))
label_template_p2 = tk.Label(window, text="参数2：")
label_template_p2.grid(row=6, column=1, padx=(10, 0))
label_template_p3 = tk.Label(window, text="参数3：")
label_template_p3.grid(row=7, column=1, padx=(10, 0))
label_template_p4 = tk.Label(window, text="参数4：")
label_template_p4.grid(row=8, column=1, padx=(10, 0))
# 4个entry
entry_template_p1 = tk.Entry(window, width=25)
entry_template_p1.grid(row=5, column=2)
entry_template_p2 = tk.Entry(window, width=25)
entry_template_p2.grid(row=6, column=2)
entry_template_p3 = tk.Entry(window, width=25)
entry_template_p3.grid(row=7, column=2)
entry_template_p4 = tk.Entry(window, width=25)
entry_template_p4.grid(row=8, column=2)


def send():
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(
        access_token)
    # headers = {"Content-type": "application/json"}
    for index in range(len(get_openid())):
        body = {
            "touser": get_openid()[index],
            "template_id": entry_template_id.get(),
            "data": {
                "thing2": {  # 机构名称
                    "value": entry_template_p1.get()
                },
                "thing8": {  # 课程名称，首字母大写
                    "value": entry_template_p2.get()
                },
                "time5": {  # 上课时间，格式：2023年9月6日 10:00~12:00
                    "value": entry_template_p3.get()
                }
            }
        }
        res_json = requests.post(url, json=body).json()
        # print(res_json)
        log = get_openid()[index]+" 推送成功\n"
        text_log.insert("-1.-1", log)


def confirm():
    msgbox = tkinter.messagebox.askokcancel(title="警告",message="确认推送吗？")
    if msgbox == True:
        send()


# ======点击推送按钮/推送日志=====================================================
button_send = tk.Button(window, text="点击推送", command=confirm)
button_send.grid(row=9, column=0, padx=(10, 0), pady=10)
label_log = tk.Label(window, text="推送结果：")
label_log.grid(row=9, column=1, padx=(10, 0), pady=10)
text_log = tk.Text(window, width=40, height=16, relief="sunken", borderwidth=1)
text_log.grid(row=9, column=2, padx=(10, 0), pady=10)

window.mainloop()
