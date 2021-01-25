from datetime import datetime
import random


def unique_order_no_generator(instance):
    
    dt = datetime.now()
    serialnum = '%04d%02d%02d%02d%02d%02d' % (dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
    ran_list = random.randint(0,9999)
    serialnum += '%04d' % (ran_list)

    order_new_id = serialnum
    return order_new_id