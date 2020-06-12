#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:38
# @Author  : Zhangyp
# @File    : zt_product_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db


class ProductModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_product'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(90))
	code = db.Column(db.String(45))
	status = db.Column(db.String(30))  # 产品状态
	desc = db.Column(db.String(256))
	PO = db.Column(db.String(30))
	deleted = db.Column(db.Enum('0', '1'))
	
	def __init__(self, _id, name, code, status, deleted):
		self.id = _id
		self.name = name
		self.code = code
		self.status = status
		self.deleted = deleted
	
	# 获取产品列表
	@classmethod
	def query_all(cls):
		return cls.query.filter_by(status='normal', deleted='0').all()
