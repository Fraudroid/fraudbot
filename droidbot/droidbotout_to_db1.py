# --*-- encoding:utf-8 --*--
'''
Created on 2016-12-30
@author: dongfeng
@summary: get apk info using aapt
'''
import os
import redis

def main():
    filelist = []
    r1 = redis.Redis(host='192.168.3.70', port=6379, db=1)
    filenames = os.listdir('/home/user/out4/')
#    print filenames
    for f in filenames:
        r1.lpush('apk_name', f)
        print f

if __name__ == '__main__': main()  #程序入口