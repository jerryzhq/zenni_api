'''
@Project ：zenni_api 
@File   :conftest.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/12 2:33 PM

'''
import pytest
from conmons.yaml_util import Yaml
# #打开yaml文件
# def read_yaml():
#     return [{"微微":"12","小强":"21"},{"娃哈哈":"123"}]


@pytest.fixture(scope="function",autouse=True)
def fix_sql(request):
    print("开始前执行")


@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    Yaml.clear_extract_yaml()