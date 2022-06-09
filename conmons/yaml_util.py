'''
@Project ：zenni_api 
@File   :yaml_util.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/12 4:03 PM

'''
import os

import yaml


class Yaml:

    def read_testcase_yaml(yaml_path):
        # mode="r" 只读
        with open(os.getcwd()+yaml_path,encoding="utf-8",mode="r") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader) #yaml.FullLoader  加载所有数据
            return value

    # 通过key读取这个文件
    def read_extract_yaml(key):
        # mode="r" 只读
        with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="r") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader) #yaml.FullLoader  加载所有数据
            return value[key]


    # 将数据写入yaml文件
    def writ_extract_yaml(data):
        # mode="a" 追加   mode='w' 写入
        with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="w") as f:
            yaml.dump(data,stream=f,allow_unicode=True)

    # 清空yaml文件
    def clear_extract_yaml():
        # mode="a" 追加   mode='w' 写入
        with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="w") as f:
            f.truncate()