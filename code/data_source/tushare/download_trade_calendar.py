# -*- coding:utf-8 -*-
# @Time     : 2020/8/29 15:01
# @Author   : 胡远
# @Github   : https://github.com/QuixoteHY
# @Email    : quixotehy@qq.com
# @Describe :

from . import tushare_client


def run(config, exchange='', start_date='', end_date=''):
    df = tushare_client.query('trade_cal', exchange=exchange, start_date=start_date, end_date=end_date)
    for index, row in df.iterrows():
        if row['is_open']:
            print(row['cal_date'], row['is_open'])


