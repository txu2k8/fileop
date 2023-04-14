#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:utils
@time:2023/4/14
@email:tao.xu2008@outlook.com
@description: 
"""
import arrow


def date_str_calc(date_step=1, start_date="2023-01-01"):
    return arrow.get(start_date).shift(days=date_step).datetime.strftime("%Y-%m-%d")


if __name__ == '__main__':
    pass
