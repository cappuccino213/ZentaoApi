#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 11:28
# @Author  : Zhangyp
# @File    : qa_tasktype.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.qa_tasktype_model import TaskTypeModel
from mid_process.data_fields import tasktype_fields
from mid_process.response_json import response


class QaTaskType(Resource):
	@staticmethod
	def get():  # 获取测试组用户列表
		tasktype = TaskTypeModel.query_list()
		if tasktype:
			data = marshal(tasktype, tasktype_fields)
			return response(True, data, "获取到测试组用户列表")
		else:
			return response(True, None, "未获取测试组用户列表")