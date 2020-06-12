#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 17:40
# @Author  : Zhangyp
# @File    : zt_project_statistics_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from db import db


class ZtProjectStatisticsModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_project_statistics'
	
	project = db.Column(db.Integer,primary_key=True)
	assignedTo = db.Column(db.String)
	estimate = db.Column(db.Float)
	consumed = db.Column(db.Float)
	left = db.Column(db.Float)
	
	@classmethod
	def query_checkbox(cls, project=None, assignedTo=None):
		if assignedTo is None:
			assignedTo = []
		if project is None:
			project = []
		result = cls.query.filter_by()
		if project:
			result = result.filter(cls.project.in_(project))
		if assignedTo:
			result = result.filter(cls.assignedTo.in_(assignedTo))
		return result.all()


if __name__ == '__main__':
	u = ZtProjectStatisticsModel
	r = u.query_checkbox(assignedTo=['wjj'])
	# r1 = u.query_by_account('zyp')
	print(type(r), r)
