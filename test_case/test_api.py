'''
@Project ：zenni_api 
@File   :test_api.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/6 4:23 PM

'''
import re
import jsonpath
import pytest
import requests
# import conmons.evn as common
from conmons.requests_util import RequestsUtil
from conmons.yaml_util import Yaml



class TestApi:
    #类变量
    access_token =""
    csrf_token = ""
    session = requests.session()


    # def test_token(self):
    #     urls = "https://uat.zenni.cn/magento/rest/default/V1/zenni/customer/login/pass"
    #     params = {
    #         "prefix": "86",
    #         "telephone": "15003676769",
    #         "password": "Aikuia123456"
    #     }
    #     # res = RequestsUtil().all_request(method=methods,url=urls,data=params)
    #     res = requests.post(url=urls, params=params)
    #     print(f'获取到的值是：{res.json()}')



    #获取token
    @pytest.mark.run(order=1)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("args_name",Yaml.read_testcase_yaml("/test_case/get_token.yaml"))
    def test_get_token(self,args_name):
        print(args_name)
        urls = args_name["request"]["url"]
        methods = args_name["request"]["method"]
        params = args_name["request"]["data"]
        res = RequestsUtil().all_request(method=methods,url=urls,params=params)
        print(f'获取到的值是：{res.json()}')
        print(f'状态码是:{res.status_code}')
        result = res.json()
        if isinstance(result, str) and len(result) == 32:
            extract_value = {"bearer":res.json()}
            Yaml.writ_extract_yaml(extract_value)







    #点击个人中心
    # def test_access_center(self):
    #     urls = "https://uat.zenni.cn/magento/rest/default/V1/zenni/customer/personal/center"
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f'bearer {Yaml.read_extract_yaml("bearer")}'
    #     }
    #     res = RequestsUtil().all_request(method="get",url=urls, headers=headers)
    #     # res = common.get_params(url=urls, headers=headers)
    #     print(res.json())

    #将商品加入购物车
    # def test_add_cart(self):
    #     urls = "/V1/zenni/customer/order/cart/do/2"
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"bearer {TestApi.access_token}"
    #     }
    #     res = common.get_params(urls,headers=headers)
    #     print(res.json())

    # @pytest.mark.smoke
    # def test_phpwind(self, fix_sql):
    #     urls = "http://47.107.116.139/phpwind"
    #     # res = requests.get(url=urls)
    #     # res = TestApi.session.get(url=urls)
    #     res = RequestsUtil().all_request("get", url=urls)
    #     result = res.text
    #     TestApi2.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)
    #     # print(res.text)
    #     print(f"fix_sql={fix_sql}")

    #登录接口
    # @pytest.mark.usermanage
    # def test_login(self):
    #     urls = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     datas = {
    #         "username": "jerry123",
    #         "password": "0301zhq",
    #         "csrf_token":TestApi.csrf_token,
    #         "backurl":"http://47.107.116.139/phpwind/",
    #         "invite":""
    #     }
    #     headers = {
    #         "Accept": "application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     # res = requests.post(url=urls,data=datas,headers=headers)
    #     # res = TestApi.session.post(url=urls,data=datas,headers=headers)
    #     res = RequestsUtil().all_request("post", url=urls, data=datas, headers=headers)
    #     print(res.text)




