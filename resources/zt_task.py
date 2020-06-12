#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 14:50
# @Author  : Zhangyp
# @File    : zt_task.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_task_model import ZtTaskModel
from mid_process.request_parse import task_args
from mid_process.data_fields import task_fields
from mid_process.response_json import response


class Task(Resource):
	@staticmethod
	def post():
		body = task_args()
		task = ZtTaskModel.query_checkbox(body['id'], body['openedBy'], body['assignedTo'], body['finishedBy'],
										  body['dateType'], body['beginDate'], body['endDate'],body['project'],body['status'])
		if task:
			data = marshal(task, task_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")