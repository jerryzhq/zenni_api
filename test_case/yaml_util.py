'''
@Project ：zenni_api 
@File   :yaml_util.py
@IDE  ：PyCharm
@Author :jerry
@Date   :2022/4/6 4:23 PM

'''
import yaml


class YamlUtil:

    def __init__(self,yaml_file):
        """
            通过init方法把yaml文件传入到这个类
        """
        self.yaml_file = yaml_file

    #读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file,encoding='utf-8') as f:
            value = yaml.load(f,Loader=yaml.FullLoader)
            print(value,type(value))

if __name__ == '__main__':
    YamlUtil('get_token.yaml').read_yaml()



