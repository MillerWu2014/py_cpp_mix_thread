# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :main_threading.py
# target    :
# 
# output    :
# author    :Miller
# date      :2019/6/25 17:09
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor


def f(a):
    while 1:
        pass


if __name__ == '__main__':
    pool = ThreadPoolExecutor()
    pool.map(f, range(100))
