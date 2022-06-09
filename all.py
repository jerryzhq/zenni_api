'''
@Project ：zenni_api 
@File   :all.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/6 4:11 PM

'''
import os
import time

import pytest
from conmons.yaml_util import Yaml
if __name__ == '__main__':
    pytest.main()
    # print(read_testcase_yaml("/test_case/get_token.yaml"))

    time.sleep(3)
    os.system("allure generate ./temps -o ./repost --clean")