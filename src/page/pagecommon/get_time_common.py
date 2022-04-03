"""
@author: DT_testing
@file:   get_time_common.py
@desc:  【】
@step：  
"""
import time

from common.base import Base
import random

class GetTimeCommon(Base):
    def get_time(self):
        # 格式化时间，按照 2017-04-15_13:46:32的格式打印出来
        new_time = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        # print(new_time)
        return new_time

    #获取随机数字
    def get_number(self):
        number=time.strftime('%y%m%d%H%M%S', time.localtime())
        return str(number)

    # 获取13、14、15、16、17、18、19开头的随机11位号码
    # ^(((13[0-9]{1})|(15[0-9]{1})|(16[0-9]{1})|(17[3-8]{1})|(18[0-9]{1})|(19[0-9]{1})|(14[5-7]{1}))+\s*\d{4}\s*\d{4})
    def get_mobile(self):
        num=time.strftime('%d%H%M%S', time.localtime())
        ran=random.randint(0,9)
        list=['13','14','15','16','17','18','19']
        first=random.choice(list)
        # 0831 修改手机号格式
        if first == '14':
            ran1 = random.randint(5, 7)
            mobile = str(first) + str(ran1) + str(num)
        elif first == '17':
            ran2 = random.randint(3, 8)
            mobile = str(first) + str(ran2) + str(num)
        else:
            mobile = str(first)+str(num)+str(ran)
        return mobile

