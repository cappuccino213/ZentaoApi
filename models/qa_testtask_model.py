#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 15:12
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : qa_testtask_model.py
# @Software: PyCharm
from db import db


class TestTaskModel(db.Model):
	__bind_key__ = 'qms'
	__tablename__ = 'qa_testtask'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(90))
	product = db.Column(
		db.Enum('eWordIMCIS', 'eWordRIS', 'eWordToken', 'eWordUniversal', '医学影像浏览器', '发片工作站', '影像存档与通信系统', '按需打印',
				'研发管理系统', '自动化测试平台V2'))
	project = db.Column(db.String(90))
	build_man = db.Column(db.String(90))
	owner = db.Column(db.String(90))
	smokeresult = db.Column(db.Enum('pass', 'fail'))
	reason = db.Column(db.String(1024))
	perpetrators = db.Column(db.String(90))
	tester = db.Column(db.String(90))
	starttime = db.Column(db.DateTime)
	finishedtime = db.Column(db.DateTime)
	
	def __init__(self, name, product, project, build_man, owner, smokeresult, reason, perpetrators, tester, starttime,
				 finishedtime):
		self.name = name
		self.product = product
		self.project = project
		self.build_man = build_man
		self.owner = owner
		self.smokeresult = smokeresult
		self.reason = reason
		self.perpetrators = perpetrators
		self.tester = tester
		self.starttime = starttime
		self.finishedtime = finishedtime
	
	# 获取冒烟测试列表
	@classmethod
	def query_all(cls):
		return cls.query.all()
	
	# 提交到数据库
	def add_to_db(self):
		try:
			db.session.add(self)
			db.session.commit()
		except:
			db.session.rollback()
			db.session.flush()
