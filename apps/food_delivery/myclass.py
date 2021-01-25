from datetime import datetime
import random

# 根据当前时间随机生成流水单号
class OrderCode:

    def __init__(self):
        self.serialnum = 'K123'

if __name__ == '__main__':
    obj = OrderCode()
    print(obj.serialnum)