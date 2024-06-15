import requests
import re


def get_ip():
    url = "http://myip.ipip.net"
    ip_info = requests.get(url, timeout=6).text  # 获取IP地址的详细信息
    ip = re.findall(r"\d+\.\d+\.\d+\.\d+", ip_info,
                    flags=0)  # 正则匹配xx.xx.xx.xx格式
    print("本机" + ip_info)
    return ip[0]  # 列表只有一个元素
