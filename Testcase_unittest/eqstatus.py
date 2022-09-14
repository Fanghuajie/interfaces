import json
import unittest

from ddt import file_data, ddt

import requests

from Testcase_unittest.yaml_util import YamlUtil


@ddt
class EquipmentStatus(unittest.TestCase):
    session = requests.session()

    @file_data('login.yml')
    def test01_login(self, **kwargs):
        # 使用yaml_util方法读取yaml文件值
        # value = YamlUtil('login.yaml').read_yaml()
        # method = value[0]['request']['method']
        # url = value[0]['request']['url']
        # data = value[0]['request']['data']
        # 使用ddt读取yaml值
        # print(kwargs['request']['method'])
        # print(kwargs['request']['url'])
        # print(kwargs['request']['data'])
        req = EquipmentStatus.session.request(method=kwargs['request']['method'], url=kwargs['request']['url'],
                                              data=kwargs['request']['data'])
        # req = EquipmentStatus.session.request(method=method, url=url, data=data)
        print(req.json())

    def test02_eps_list(self):
        method = 'get'
        url = "http://192.168.3.233:9090/basedata/equipstate/list"
        data = {
            "limit": 10,
            "offset": 0
        }
        # value = YamlUtil().read_extract_yaml('cookie')
        # headers = {
        #    "Cookie": value
        # }
        req = EquipmentStatus.session.request(method=method, url=url, data=data)
        # req = Test_ep_info.session.request('get', url=url, params=data, headers=headers)
        print(req.json())


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # testcases = [EquipmentStatus("test01_login")]
    # suite.addTests(testcases)
    # unittest.main(defaultTest='suite')
    unittest.main()
