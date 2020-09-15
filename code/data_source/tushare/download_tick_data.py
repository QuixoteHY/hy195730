# -*- coding:utf-8 -*-
# @Time     : 2020/9/11 11:45
# @Author   : 胡远
# @Github   : https://github.com/QuixoteHY
# @Email    : quixotehy@qq.com
# @Describe :

# from . import tushare_client
import tushare


def run(config, exchange='', start_date='2018-12-12', end_date=''):
    # df = tushare_client.get_tick_data('600848', date=start_date, src='tt')
    df = tushare.get_tick_data('600848', date=start_date, src='tt')
    print(df.head(10))
    df.to_csv('G:\hy195730\data\df1.csv')


if __name__ == '__main__':
    config = dict()
    run(config)

