#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 15:16
# @Author  : Zhangyp
# @File    : zt_bug_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from db import db
import datetime

now_date = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


class BugModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_bug'
	
	id = db.Column(db.Integer, primary_key=True)
	product = db.Column(db.Integer)
	project = db.Column(db.Integer)
	story = db.Column(db.Integer)
	task = db.Column(db.Integer)
	title = db.Column(db.String)
	severity = db.Column(db.Integer)
	pri = db.Column(db.Integer)
	type = db.Column(db.String)
	status = db.Column(db.Enum('active', 'resolved', 'closed'))
	openedBy = db.Column(db.String)
	openedDate = db.Column(db.DateTime)
	assignedTo = db.Column(db.String)
	assignedDate = db.Column(db.DateTime)
	closedBy = db.Column(db.String)
	closedDate = db.Column(db.DateTime)
	deadline = db.Column(db.Date)
	testtask = db.Column(db.Integer)  # 测试单
	resolvedBy = db.Column(db.String)  # 解决人
	resolution = db.Column(db.String)  # 解决方案
	resolvedBuild = db.Column(db.String)  # 解决版本
	resolvedDate = db.Column(db.DateTime)  # 解决日期
	deleted = db.Column(db.Enum('0', '1'))  # 测试单
	
	@classmethod
	def query_checkbox(cls, id=[], product=[], project=[], severity=[], openedBy=[], assignedTo=[], closedBy=[],
					   resolvedBy=[], dateType='resolvedDate',
					   beginDate='2018-3-28 00:00:00', endDate=now_date,status=[]):
		result = cls.query.filter_by(deleted='0')
		if id:
			result = result.filter(cls.id.in_(id))
		if product:
			result = result.filter(cls.product.in_(product))
		if project:
			result = result.filter(cls.project.in_(project))
		if severity:
			result = result.filter(cls.severity.in_(severity))
		if openedBy:
			result = result.filter(cls.openedBy.in_(openedBy))
		if assignedTo:
			result = result.filter(cls.assignedTo.in_(assignedTo))
		if closedBy:
			result = result.filter(cls.closedBy.in_(closedBy))
		if resolvedBy:
			result = result.filter(cls.resolvedBy.in_(resolvedBy))
		if dateType:
			if dateType == 'openedDate':
				result = result.filter(cls.openedDate.between(beginDate, endDate))
			if dateType == 'assignedDate':
				result = result.filter(cls.assignedDate.between(beginDate, endDate))
			if dateType == 'closedDate':
				result = result.filter(cls.closedDate.between(beginDate, endDate))
			if dateType == 'resolvedDate':
				result = result.filter(cls.resolvedDate.between(beginDate, endDate))
		if status:
			result = result.filter(cls.status.in_(status))
		return result.all()


if __name__ == '__main__':
	u = BugModel
	r = u.query_checkbox(resolvedBy=['xhyx'])
	# r1 = u.query_by_account('zyp')
	print(type(r), r)
# print(type(r1))
