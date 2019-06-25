# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :main_test.py
# target    :
# 
# output    :
# author    :Miller
# date      :2019/6/25 17:41
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
from mix_multhread import nothing
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor()

for i in range(100):
    pool.submit(nothing)

