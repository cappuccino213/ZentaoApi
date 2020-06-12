#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:38
# @Author  : Zhangyp
# @File    : zt_story_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db
import datetime

now_date = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


class StoryModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_story'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	product = db.Column(db.Integer)  # 所属产品id
	title = db.Column(db.String(255))  # 需求名称
	type = db.Column(db.String(30))  # 需求类型
	pri = db.Column(db.Integer)  # 优先级
	status = db.Column(db.Enum('', 'changed', 'active', 'draft', 'closed'))  # 当前状态
	stage = db.Column(
		db.Enum('', 'wait', 'planned', 'projected', 'developing', 'developed', 'testing', 'tested', 'verified',
				'released', 'closed'))  # 所处阶段
	openedBy = db.Column(db.String(30))  # 创建人
	openedDate = db.Column(db.DateTime)
	assignedTo = db.Column(db.String(30))  # 责任人
	assignedDate = db.Column(db.DateTime)
	reviewedBy = db.Column(db.String(30))  # 评审者
	reviewedDate = db.Column(db.DateTime)
	version = db.Column(db.Integer)  # 版本号
	closedBy = db.Column(db.String(30))
	closedDate = db.Column(db.DateTime)  # 关闭日期
	deleted = db.Column(db.Enum('0', '1'))
	
	# def __init__(self):
		# self.now_date = (datetime.now()+datetime.timedelta(days=+1)).date
		# pass
	
	# 通过id列表查询需求
	@classmethod
	def query_by_id(cls, _id=[]):
		try:
			result = cls.query.filter_by(deleted='0').filter(cls.id.in_(_id)).all()
		except:
			result = None
		return result
	
	
	# 多选条件查询
	@classmethod
	def query_checkbox(cls, product=[], openedBy=[], assignedTo=[], reviewedBy=[], dateType='closedDate',
					   beginDate='2018-3-28', endDate=now_date,status=[]):
		result = cls.query.filter_by(deleted='0')
		if product:
			result = result.filter(cls.product.in_(product))
		if openedBy:
			result = result.filter(cls.openedBy.in_(openedBy))
		if assignedTo:
			result = result.filter(cls.assignedTo.in_(assignedTo))
		if reviewedBy:
			result = result.filter(cls.reviewedBy.in_(reviewedBy))
		if dateType:
			if dateType == 'openedDate':
				result = result.filter(cls.openedDate.between(beginDate, endDate))
			if dateType == 'assignedDate':
				result = result.filter(cls.assignedDate.between(beginDate, endDate))
			if dateType == 'reviewedDate':
				result = result.filter(cls.reviewedDate.between(beginDate, endDate))
			if dateType == 'closedDate':
				result = result.filter(cls.closedDate.between(beginDate, endDate))
		if status:
			result = result.filter(cls.status.in_(status))
		return result.all()


if __name__ == '__main__':
	u = StoryModel
	r = u.query_checkbox(['001'], assignedTo=['001'])
	# r1 = u.query_by_account('zyp')
	print(type(r), r)
# print(type(r1))
