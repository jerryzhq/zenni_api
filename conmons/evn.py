'''
@Project ：zenni_api 
@File   :evn.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/6 5:53 PM

'''
import requests


def post_token(url,params=None,headers=None):
    ip = "https://uat.zenni.cn/magento/rest/default"
    r = requests.post(url=ip+url,json=params,headers=headers)
    return r

def get_params(url,params=None,headers=None):
    ip = "https://uat.zenni.cn/magento/rest/default"
    r = requests.get(url=ip+url,json=params,headers=headers)
    return r