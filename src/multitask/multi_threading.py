#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

import time

import logging


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 5
    while n <= 5:
        n = n + 1
        logging.info('----- %s ----' % n)
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.01)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
