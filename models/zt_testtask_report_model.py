#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 11:39
# @Author  : Zhangyp
# @File    : zt_testtask_report_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""测试单与测试报告link视图"""
from db import db

class TestTaskReportModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_testtask_report'
	
	task_id = db.Column(db.Integer, primary_key=True)
	task_name = db.Column(db.String(255))
	tester = db.Column(db.String(30))
	task_desc = db.Column(db.Text)
	task_status = db.Column(db.Enum('blocked', 'doing', 'wait', 'done'))
	report_id = db.Column(db.Integer)
	report_title = db.Column(db.String(255))
	reporter = db.Column(db.String(30))
	report_desc = db.Column(db.Text)
	endDate = db.Column(db.Date)
	
	# 多选条件查询
	@classmethod
	def query_checkbox(cls, begin, end, account=[]):
		result = cls.query.filter_by().order_by(TestTaskReportModel.reporter)
		if account:
			result = result.filter(cls.reporter.in_(account))
		if begin and end:
			result = result.filter(cls.endDate.between(begin, end))
		return result.all()
