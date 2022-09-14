import os

import xlrd


class ExcelUtil:

    def read_excel(self, excel_name):
        # book = xlrd.open_workbook("D:\\桌面\\Project\\PUNCH\\"+excel_name)
        book = xlrd.open_workbook(os.getcwd() + "/testdata/" + excel_name)
        sheet = book.sheets()[0]
        case = []
        for i in range(0, sheet.nrows):
            # 判断过滤掉标注的名称，是名称过滤
            if sheet.row_values(i)[0] == 'URL':
                pass
            else:
                #  如果不是记录出来使用数据
                case.append(sheet.row_values(i))
        return case
