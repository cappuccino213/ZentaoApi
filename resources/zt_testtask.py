#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 10:41
# @Author  : Zhangyp
# @File    : zt_testtask.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, marshal
from models.zt_testtask_model import TestTaskModel
from mid_process.request_parse import testtask_args
from mid_process.data_fields import testtask_fields
from mid_process.response_json import response


class TestTask(Resource):
	@staticmethod
	def get():  # 获取测试组用户列表
		args = testtask_args()
		testtask = TestTaskModel.query_by_id(args['id'])
		if testtask:
			data = marshal(testtask, testtask_fields)
			return response(True, data, "获取测试单")
		else:
			return response(True, None, "未获取测试单")