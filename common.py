#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 14:50
# @Author  : Shijun Gong
# @Version    : 0.1.0
# @File    : common.py
# @Software: PyCharm

def read_conf():
    un = ''
    pw = ''
    ip = ''
    try:
        with open('user.conf', 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line == '':
                    continue
                if line[0] == '#':
                    continue
                if line.split('=')[0].strip() == 'username':
                    un = line.split('=')[1].strip()
                elif line.split('=')[0].strip() == 'password':
                    pw = line.split('=')[1].strip()
                else:
                    print('user.conf is a error format. \n')
    except IOError as e:
        print('cannot read user.conf file--' + str(e) + ', please create user.conf file. \n')
    return un, pw

if __name__ == '__main__':
    print(read_conf())