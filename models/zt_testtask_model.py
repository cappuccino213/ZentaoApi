#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:38
# @Author  : Zhangyp
# @File    : zt_testtask_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""测试单"""

from db import db


class TestTaskModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_testtask'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(90))
	product = db.Column(db.Integer)
	project = db.Column(db.Integer)
	build = db.Column(db.String(30))
	owner = db.Column(db.String(30))
	begin = db.Column(db.Date)
	end = db.Column(db.Date)
	status = db.Column(db.Enum('blocked', 'doing', 'wait', 'done'))
	deleted = db.Column(db.Enum('0', '1'))
	
	# 通过id获取测试单列表
	@classmethod
	def query_by_id(cls, _id):
		return cls.query.filter_by(id=_id, deleted='0').first()
