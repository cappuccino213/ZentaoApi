#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 13:40
# @Author  : Zhangyp
# @File    : zt_project_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db


class ProjectModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_project_view'
	
	id = db.Column(db.Integer, primary_key=True)
	project_name = db.Column(db.String(90))
	PM = db.Column(db.String(30))
	product = db.Column(db.Integer)
	team_members = db.Column(db.String(90))
	
	@classmethod
	def query_checkbox(cls, _id=(), project_name=(), pm=(), product=(), team_members=None):
		result = cls.query.filter_by()
		if _id:
			result = result.filter(cls.id.in_(_id))
		if project_name:
			result = result.filter(cls.project_name.in_(project_name))
		if pm:
			result = result.filter(cls.PM.in_(pm))
		if product:
			result = result.filter(cls.product.in_(product))
		if team_members:
			result = result.filter(cls.team_members.like('%'+team_members+'%'))
		return result.all()
