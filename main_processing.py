# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :main_processing.py
# target    :
# 
# output    :
# author    :Miller
# date      :2019/6/25 17:08
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
from concurrent.futures import ProcessPoolExecutor


def f(a):
    while 1:
        pass


if __name__ == '__main__':
    pool = ProcessPoolExecutor()
    pool.map(f, range(100))
