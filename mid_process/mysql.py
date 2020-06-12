#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 16:31
# @Author  : Zhangyp
# @File    : mysql.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""用于复杂的sql查询，不走ORM的模式"""
from config import DB_INFO


def query(sql):
	import pymysql
	my_db = pymysql.connect(**DB_INFO)
	cursor = my_db.cursor()
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()
		my_db.close()
		return results
	except Exception as e:
		raise ('Error: unable to fecth data' + ',reason:{}'.format(str(e)))
