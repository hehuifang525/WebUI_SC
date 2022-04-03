from time import sleep
from  selenium.webdriver.common.by import By

from common.base import Base
import xlrd

class OperationExcel(Base):

    # def choose_excel(self, route, sheetname, sectionname):
    #     '''
    #     读取excel中的数据，逐行读取
    #     :param route: 读取excel文件的路径
    #     :param sheetname: 读取excel文件的sheet名称
    #     :return: 返回读取的excel文件列表，列表中以字典的方式存储
    #     '''
    #     usertable = xlrd.open_workbook(route)
    #     # 2 打开sheet
    #     usersheet = usertable.sheet_by_name(sheetname)
    #     # 3 获取表的行、列数
    #     rows = usersheet.nrows
    #     cols = usersheet.ncols
    #     # print(rows, cols)
    #     # 4 将读取数据放入列表中，输入所有列表
    #     # 读行，并追加到列表中
    #     datelist = []
    #     start_flag = 0
    #     end_flag = 0
    #     page = None
    #     for i in range(0, rows):
    #         # print('取一次行数据')
    #         # 跳过第一行
    #         if i == 0:
    #             pass
    #         else:
    #             # 读取文件的方式需要修改
    #             data1 = usersheet.row_values(i, 0)
    #             if data1[0] == sectionname:
    #                 data2 = {'name': data1[1], 'type': data1[2], 'value': data1[3]}
    #                 datelist.append(data2)
    #
    #     return datelist
    #
    # 检查整个页面中元素是否存在
    # def check_element(self, userlist02):
    #
    #     notexcitlist02 = []
    #     # 1读取表格元素
    #     for i in range(0, len(userlist02) - 1):
    #         ele = None
    #         try:
    #             if userlist02[i].get('type') == 'id':
    #                 loc = (By.ID, userlist02[i].get('value').strip())
    #                 ele = self.find_element(loc)
    #             elif userlist02[i].get('type') == 'css':
    #                 loc = (By.CSS_SELECTOR, userlist02[i].get('value').strip())
    #                 ele = self.find_element(loc)
    #         except:
    #             pass
    #         if ele == None:
    #             notexcitlist02.append(userlist02[i])
    #     return notexcitlist02

    def read_excel_value(self, route, sheetname):
        '''
        读取excel中的数据，逐行读取
        :param route: 读取excel文件的路径，每个模块读取一次excel
        :param sheetname: 读取excel文件的sheet名称
        :return: 返回读取结果，以序列形式返回
          [{"sectionname":'A',"name":'A',"type":'A',""value:'A'},{..}]
          sectionname 对应excel“页面”字段
          name 对应excel“元素名称”字段
          type 对应excel“类型”字段
          value 对应excel“值”字段
        '''
        usertable = xlrd.open_workbook(route)
        # 2 打开sheet
        usersheet = usertable.sheet_by_name(sheetname)
        # 3 获取表的行、列数
        rows = usersheet.nrows
        cols = usersheet.ncols
        # print(rows, cols)
        # 4 将读取数据放入列表中，输入所有列表
        # 读行，并追加到列表中
        datelist = []
        for i in range(0, rows):
            # print('取一次行数据')
            # 跳过第一行
            if i == 0:
                pass

            else:
                # 读取文件的方式需要修改
                data1 = usersheet.row_values(i, 0)
                # if data1[0] == sectionname:
                data2 = {'sectionname': data1[0], 'name': data1[1], 'type': data1[2], 'value': data1[3]}
                # 跳过不确定的元素-占位元素
                if data1[3] == 'pass':
                    pass
                else:
                    datelist.append(data2)

        return datelist

    def check_element_whether_exists(self, datelist, sectionname):
        '''
         检查excel中记录的元素在指定页面是否存在
        :param datelist: 读取excel的返回值
        :param sectionname: 取excel中的页面名称，如“默认页面、添加页面”
        :return:返回不存在元素的列表[{"sectionname":'A',"name":'A',"type":'A',""value:'A'},{..}]
        同时将返回转格式输出
        '''
        non_existent_list =[]
        # 1读取表格元素
        for i in range(0, len(datelist)):
            # print('循环次数：', len(datelist))

            if datelist[i].get('sectionname') == sectionname:
                # print('元素值：', datelist[i].get('name'))
                ele = None
                try:
                    if datelist[i].get('type') == 'id':
                        # print(i,'1id')
                        loc = (By.ID, datelist[i].get('value').strip())
                        ele = self.find_element_10(loc)

                    elif datelist[i].get('type') == 'css':
                        # print('2css')
                        loc = (By.CSS_SELECTOR, datelist[i].get('value').strip())
                        ele = self.find_element_10(loc)
                    elif datelist[i].get('type') == 'xpath':
                        loc = (By.XPATH, datelist[i].get('value').strip())
                        ele = self.find_element_10(loc)

                except:
                    pass
                # 如果在页面中查找不到该元素，则将查找的元素添加
                if ele == None:
                    non_existent_list.append(datelist[i])
            else:
                # 中断，所以同一页面的元素需要写到一起
                pass

        # 对non_existent_list进入处理输出
        non_exist_info = ''
        for i in range(0, len(non_existent_list)):
            sectionname = non_existent_list[i].get('sectionname')
            name = non_existent_list[i].get('name')
            type = non_existent_list[i].get('type')
            value = non_existent_list[i].get('value')
            non_exist_info = non_exist_info + (sectionname+name +'缺' + type+ ':'+value+";")
            # print(info)
        non_exist_info ="当前不符合项数量：" + str(len(non_existent_list)) +"，分别为："+ non_exist_info
        non_exist_num = len(non_existent_list)
        return non_exist_info, non_exist_num


    def non_existent_list_print(self,non_existent_list):
        '''
            对列表[{"sectionname":'A',"name":'A',"type":'A',""value:'A'},{..}]进行转换打印，提高可读性
        '''
        for i in range(0, len(non_existent_list)):
            sectionname = non_existent_list[i].get('sectionname')
            name = non_existent_list[i].get('name')
            type = non_existent_list[i].get('type')
            value = non_existent_list[i].get('value')
            info = sectionname + '的'+ name +'缺少值 ' + type+ ':'+value
            print(info)
