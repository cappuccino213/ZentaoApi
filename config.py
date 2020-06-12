#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 16:24
# @Author  : Zhangyp
# @File    : config.py.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""数据库相关配置"""
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:123456@192.168.1.43:3306/zentao?charset=UTF8"

# 多数据库时引用绑定来区分
SQLALCHEMY_BINDS = {'zentao': "mysql+pymysql://test:123456@192.168.1.43:3306/zentao?charset=UTF8MB4",
					'qms': "mysql+pymysql://test:123456@192.168.1.16:3306/new_weeklyreport?charset=UTF8MB4"}

# SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = True

# Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
SQLALCHEMY_TRACK_MODIFICATIONS = True

"""不走ORM连接"""
DB_INFO = {"host": "192.168.1.43",
		   "user": "test",
		   "password": "123456",
		   "port": 3306,
		   "db": "zentao",
		   "charset": 'utf8'
		   }
