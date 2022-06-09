'''
@Project ：zenni_api 
@File   :requests_util.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/12 2:54 PM

'''
import requests


class RequestsUtil:

    session = requests.session()

    def all_request(self,method,url,**kwargs):
        res = RequestsUtil.session.request(method,url,**kwargs)
        return res