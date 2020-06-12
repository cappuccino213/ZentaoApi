#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:40
# @Author  : Zhangyp
# @File    : zt_testreport_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db


class TestReportModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_testreport'
	
	id = db.Column(db.Integer, primary_key=True)
	product = db.Column(db.Integer)
	project = db.Column(db.Integer)
	tasks = db.Column(db.String(255))  # 测试单号
	build = db.Column(db.String(255))  # 版本
	title = db.Column(db.String(255))  # 标题
	createBy = db.Column(db.String(30))  # 创建人
	deleted = db.Column(db.Enum('0', '1'))
