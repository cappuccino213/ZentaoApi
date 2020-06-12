#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 15:44
# @Author  : Zhangyp
# @File    : zt_bug.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_bug_model import BugModel
from mid_process.request_parse import bug_args
from mid_process.data_fields import bug_fields
from mid_process.response_json import response


class Bug(Resource):
	@staticmethod
	def post():
		body = bug_args()
		bug = BugModel.query_checkbox(body['id'], body['product'], body['project'],body['severity'], body['openedBy'],
									  body['assignedTo'], body['closedBy'], body['resolvedBy'],
									  body['dateType'], body['beginDate'], body['endDate'],body['status'])
		
		if bug:
			data = marshal(bug, bug_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")
