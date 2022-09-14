import json
import re
import pytest
from Testcase.excel_util import ExcelUtil
from common.request_util import RequestUtil
from common.yaml_util import YamlUtil


class Test_ep_info:
    # 在每个用例前执行
    def setup(self):
        print("start")

    # 在每个用例后执行
    def teardown(self):
        print("end")
    #类变量通过类名访问
    #cookie = ""

    @pytest.mark.smoke
    @pytest.mark.parametrize("url,data,method,module,name,code,msg", ExcelUtil().read_excel("test_01.xls"))
    def test_login(self, url, data, method, module, name, code, msg, conn_database):
        # method = 'post'
        # url = "http://192.168.3.233:9090/login"
        # data = {
        #     "username": "admin",
        #     "password": "123456"
        # }
        # headers = {
        #     "Content-Type": "application/json"
        # }
        req = RequestUtil().request_api(method=method, url=url, data=json.loads(data))
        # print(type(req))
        # req = requests.session().request('post', url=url, data=data) # request 封装之前的
        # 提取登录成功后的cookie，写入到extract.yml文件中
        if req.json()["code"] == 0:
            cookie1 = req.headers['Set-Cookie']
            cks = re.findall(r"GMT, (.+?); Path=/;", cookie1)[0]  # 使用正则表达式提取cookie
            YamlUtil().write_extract_yaml({'cookie': cks})
            print(cks)
        # 断言
        assert req.json()['msg'] == msg
        assert req.json()['code'] == code
        print(req.json()['msg'])
        # assert req.json()["code"] == 0

    def test_get_ep_list(self):
        method = 'get'
        url = "http://192.168.3.233:9090/basedata/equipgroup/list"
        data = {
            "limit": 10,
            "offset": 0
        }
        # value = YamlUtil().read_extract_yaml('cookie')
        # headers = {
        #    "Cookie": value
        # }
        req = RequestUtil().request_api(method, url, data)
        # req = Test_ep_info.session.request('get', url=url, params=data, headers=headers)
        print(req.json())

    @pytest.mark.parametrize("eqinfo", YamlUtil().read_data_yaml("eq_data.yml"))
    def test_new_eq(self, eqinfo):
        print(eqinfo)
        method = eqinfo['request']['method']
        url = eqinfo['request']['url']
        data = eqinfo['request']['data']
        # url = "http://192.168.3.233:9090/basedata/equipgroup/save"
        # data = {
        #     "egCode": "111",
        #     "egName": "012",
        #     "egFlag": "123",
        #     "remark": "remark",
        #     "isInvalid": 0
        # }
        # value = YamlUtil().read_extract_yaml('cookie')
        # headers = {
        #    "Cookie": value
        # }
        req = RequestUtil().request_api(method, url, data)
        # req = Test_ep_info.session.request(method, url=url, data=data)
        print(req.json())

