# -*- coding:utf-8 -*-
# @Time     : 2020/8/29 15:09
# @Author   : 胡远
# @Github   : https://github.com/QuixoteHY
# @Email    : quixotehy@qq.com
# @Describe :

from config import Config

from data_source import download_trade_calendar


def run():
    download_trade_calendar.run(Config, exchange='CZCE')


if __name__ == '__main__':
    run()

