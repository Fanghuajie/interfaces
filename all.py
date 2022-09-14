import logging
import os
import sys
import time

import pytest
from Testcase.Email import EmailManage

if __name__ == '__main__':
    # pytest.main(["-vs", '-n=2'])
    # pytest.main(["-vs", '--reruns==2'])
    # pytest.main()
    # os.system("allure generate temp -o reports --clean")
    file = os.path.basename(sys.argv[0])
    # print(file)
    # print(sys.argv[0])
    logging.basicConfig(
        level=logging.info(),
        format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
        datafomat='%a, %d %b %Y %H: %M: %S',
        filemode='w'
    )
    try:
        print("开始执行脚本")
        logging.info("===============" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "================")
        #每次生成数据前先清空数据
        pytest.main([r'E:\python_pythoncharm\Testcase', "--alluredir=./temp", "--clean-alluredir"])
        logging.info("脚本执行完成")
    except Exception as e:
        logging.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)
    try:
        print("开始执行报告生成")
        os.system("allure generate temp -o reports --clean")
        # logger.info("报告生成完毕")
        print("报告生成完毕")
        time.sleep(8)
        EmailManage().send_mail('E:\\python_pythoncharm\\reports\\index.html')

    except Exception as e:
        print("报告生成失败，请重新执行", e)
        # logger.error("报告生成失败，请重新执行", e)
        # log.error('执行用例失败，请检查环境配置')
        raise
    time.sleep(5)
