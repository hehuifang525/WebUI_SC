# 封装配置文件
from configparser import ConfigParser
import os.path


class HandleConfig:
    """
    配置文件读写数据的封装
    注释comment_prefixes调整：当注释标识为#，写入ini则被删除；当注释标识为;，写入ini则被保留；

    使用示例：
    #引用
    from common.HandleConfig import HandleConfig
    #读取
    value = HandleConfig().read_config("session", "option")
    #写入
    HandleConfig().write_config("session","option","value")
    """
    def __init__(self):
        dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.cfgpath = dir + '/data/config.ini'
        # 获取配置文件路径
        self.config = ConfigParser(comment_prefixes='#', allow_no_value=True)        # 读取配置文件1.创建配置解析器
        self.config.read(self.cfgpath, encoding="utf-8")   # 读取配置文件2.指定读取的配置文件

    # read_config获取所有的字符串，section区域名, option选项名
    def read_config(self, section, option):
        # print(self.config.sections(),self.config.options("url"))
        return self.config.get(section, option)

    def write_config(self, section, option, values):
        """
        写入配置操作
        :param section: 需要写入数据的section
        :param option: 需要写入数据的option,有则写入，无则创建
        :param values: 需要的数据
        :return:
        """
        self.config.set(section, option, values)
        self.config.write(open(self.cfgpath, "w", encoding="utf-8"))


# # 使用示例
# if __name__ == '__main__':
#
#     # 读取
#     # value = HandleConfig().read_config("session", "option")
#
#     # 写入
#     HandleConfig().write_config("url","option","value")




