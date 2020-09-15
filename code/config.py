# -*- coding:utf-8 -*-
# @Time     : 2020/8/29 22:31
# @Author   : 胡远
# @Github   : https://github.com/QuixoteHY
# @Email    : quixotehy@qq.com
# @Describe :

import os


class Config:
    # 交易所

    # 数据存储位置
    data_path = r"G:\hy195730\data"
    data_trade_calendar_path = r"G:\hy195730\data\trade_calendar"

    # 文件名称
    filename_trade_calendar_czce = os.path.join(data_trade_calendar_path, 'trade_calendar_cace.csv')
    filename_trade_calendar_shfe = os.path.join(data_trade_calendar_path, 'trade_calendar_shfe.csv')
    filename_trade_calendar_dce = os.path.join(data_trade_calendar_path, 'trade_calendar_dce.csv')
    filename_trade_calendar_cffex = os.path.join(data_trade_calendar_path, 'trade_calendar_cffex.csv')

    # 日志输出位置
    log_path = r"G:\hy195730\log"


print('[INFO] Config check begin...')
for name, value in vars(Config).items():
    print('[INFO] %s=%s' % (name, value))
    if name.endswith('_path'):
        if not os.path.exists(value):
            os.makedirs(value)
print('[INFO] Config check end...\n')

