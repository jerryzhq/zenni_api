'''
@Project ：zenni_api 
@File   :test_api.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/6 4:23 PM

'''
import re

import pytest
import requests
import conmons.evn as common
from conmons.requests_util import RequestsUtil

class AATestApi2:
    #类变量
    access_token =""
    csrf_token = ""
    session = requests.session()


    @pytest.mark.smoke
    def test_phpwind(self,fix_sql):
        urls = "http://47.107.116.139/phpwind"
        # res = requests.get(url=urls)
        # res = TestApi.session.get(url=urls)
        res = RequestsUtil().all_request("get",url=urls)
        result = res.text
        TestApi2.csrf_token = re.search('name="csrf_token" value="(.*?)"',result).group(1)
        # print(res.text)
        print(f"fix_sql={fix_sql}")

    #登录接口
    @pytest.mark.usermanage
    def test_login(self):
        urls = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        datas = {
            "username": "jerry123",
            "password": "0301zhq",
            "csrf_token":TestApi2.csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        # res = requests.post(url=urls,data=datas,headers=headers)
        # res = TestApi.session.post(url=urls,data=datas,headers=headers)
        res = RequestsUtil().all_request("post", url=urls, data=datas, headers=headers)
        print(res.text)




