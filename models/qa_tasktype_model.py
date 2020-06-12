#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 11:20
# @Author  : Zhangyp
# @File    : qa_tasktype_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db


class TaskTypeModel(db.Model):
	__bind_key__ = 'qms'
	__tablename__ = 'qa_tasktype'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	type = db.Column(db.String(40))
	
	@classmethod
	def query_list(cls):
		return cls.query.all()
	
	
