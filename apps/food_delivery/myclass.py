from datetime import datetime
import random

# 根据当前时间随机生成流水单号
class OrderCode:
    # 构造函数
    def __init__(self):
        self.serialnum = ''  # 存储生成的单号，默认为空
        # 自动执行函数
        self.get_serialnum()

    def get_serialnum(self):
        """生成订单号"""
        # 获取当前系统时间
        dt = datetime.now()
        # 生成订单号
        self.serialnum = '%04d%02d%02d%02d%02d%02d' % (dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
        # 生成4位随机数字
        ran_list = random.randint(0,9999)
        # 随机数附加到尾部
        self.serialnum += '%04d' % (ran_list)


# if __name__ == '__main__':
#     obj = OrderCode()
#     print(obj.serialnum)