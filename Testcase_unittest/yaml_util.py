import os

import yaml


class YamlUtil:

    # 读取extract.yaml文件
    def __init__(self, file_path):
        self.file_path = file_path

    # 读取extract.yaml文件
    def read_yaml(self):
        with open(self.file_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            return value

    # 写入extract.yaml文件
    def write_yaml(self, data):
        with open(self.file_path, mode="a", encoding="utf-8") as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)