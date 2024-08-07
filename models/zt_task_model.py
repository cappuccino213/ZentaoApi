#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:36
# @Author  : Zhangyp
# @File    : zt_task_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db
import datetime

now_date = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


class ZtTaskModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_task_view'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	parent = db.Column(db.Integer)
	parentName = db.Column(db.String)
	project = db.Column(db.Integer)
	# module = db.Column(db.Integer)
	name = db.Column(db.String)
	type = db.Column(db.String)
	pri = db.Column(db.Integer)
	deadline = db.Column(db.Date)
	status = db.Column(db.Enum('wait', 'doing', 'done', 'pause', 'cancel', 'closed'))
	desc = db.Column(db.Text)
	openedBy = db.Column(db.String)
	openedDate = db.Column(db.DateTime)
	assignedTo = db.Column(db.String)
	assignedDate = db.Column(db.DateTime)
	estStarted = db.Column(db.Date)  # 预计开始
	realStarted = db.Column(db.Date)
	finishedBy = db.Column(db.String)  # 完成者
	finishedDate = db.Column(db.DateTime)
	deleted = db.Column(db.Enum('0', '1'))
	
	# @classmethod
	# def query_checkbox(cls, _id=[], openedBy=[], assignedTo=[], finishedBy=[], dateType='finishedDate',
	# 				   beginDate='2018-3-28 00:00:00', endDate=now_date, project=[],status=[]):
	# 	result = cls.query.filter_by(deleted='0')
	# 	if _id:
	# 		result = result.filter(cls.id.in_(_id))
	# 	if openedBy:
	# 		result = result.filter(cls.openedBy.in_(openedBy))
	# 	if assignedTo:
	# 		result = result.filter(cls.assignedTo.in_(assignedTo))
	# 	if finishedBy:
	# 		result = result.filter(cls.finishedBy.in_(finishedBy))
	# 	if dateType:
	# 		if dateType == 'openedDate':
	# 			result = result.filter(cls.openedDate.between(beginDate, endDate))
	# 		if dateType == 'assignedDate':
	# 			result = result.filter(cls.assignedDate.between(beginDate, endDate))
	# 		if dateType == 'finishedDate':
	# 			result = result.filter(cls.finishedDate.between(beginDate, endDate))
	# 	if project:
	# 		result = result.filter(cls.project.in_(project))
	# 	if status:
	# 		result = result.filter(cls.status.in_(status))
	# 	return result.all()


	# 优化代码
	@classmethod
	def query_checkbox(cls, _id=None, openedBy=None, assignedTo=None, finishedBy=None,
					   dateType='finishedDate', beginDate='2018-3-28 00:00:00',
					   endDate=now_date, project=None, status=None):
		if _id is None:
			_id = []
		if openedBy is None:
			openedBy = []
		if assignedTo is None:
			assignedTo = []
		if finishedBy is None:
			finishedBy = []
		if project is None:
			project = []
		if status is None:
			status = []

		try:
			result = cls.query.filter_by(deleted='0')
			if _id:
				result = result.filter(cls.id.in_(_id))
			if openedBy:
				result = result.filter(cls.openedBy.in_(openedBy))
			if assignedTo:
				result = result.filter(cls.assignedTo.in_(assignedTo))
			if finishedBy:
				result = result.filter(cls.finishedBy.in_(finishedBy))

			# 使用字典映射重构日期类型判断逻辑
			date_columns = {
				'openedDate': cls.openedDate,
				'assignedDate': cls.assignedDate,
				'estStarted':cls.estStarted,
				'finishedDate': cls.finishedDate,
			}
			if dateType in date_columns:
				result = result.filter(date_columns[dateType].between(beginDate, endDate))

			if project:
				result = result.filter(cls.project.in_(project))
			if status:
				result = result.filter(cls.status.in_(status))

			return result.all()
		except Exception as e:
			print(f"查询zt_task_view发生异常: {e}")
			return []


if __name__ == '__main__':
	u = ZtTaskModel
	r = u.query_checkbox(assignedTo=['wjj'])
	r1 = u.query_checkbox(_id=None, openedBy=None, assignedTo=['wangj'], finishedBy=None, dateType='estStarted', beginDate='2024/7/15 0:00:00', endDate='2024/7/21 23:59:59', project=None, status=None)
# {'id': None, 'openedBy': None, 'assignedTo': ['wangj'], 'finishedBy': None, 'dateType': 'estStarted', 'beginDate': '2024/7/15 0:00:00', 'endDate': '2024/7/21 23:59:59', 'project': None, 'status': None}