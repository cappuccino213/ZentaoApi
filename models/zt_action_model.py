#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 14:20
# @Author  : Zhangyp
# @File    : zt_action_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from db import db


class ActionModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_action'
	
	id = db.Column(db.Integer, primary_key=True)
	objectType = db.Column(db.String(30))
	objectID = db.Column(db.Integer)
	product = db.Column(db.String(255))
	project = db.Column(db.Integer)
	actor = db.Column(db.String(100))
	action = db.Column(db.String(30))
	date = db.Column(db.DateTime)
	comment = db.Column(db.String(255))
	extra = db.Column(db.String(30))
	read = db.Column(db.Enum('0', '1'))
	efforted = db.Column(db.SmallInteger)
	
	@classmethod
	def query_story_extra(cls, user, beginDate, endDate):
		result = cls.query.filter_by(objectType='story').filter_by(extra=user).filter(
			cls.date.between(beginDate, endDate))
		return result.all()


if __name__ == '__main__':
	u = ActionModel
	r = u.query_story_extra('xxy', '2019-12-24 14:27:17', '2020-12-24 14:27:18')
	# print(type(r.objectID), r.objectID)
	r1 = [i.objectID for i in r]
	print(type(r1), r1)
