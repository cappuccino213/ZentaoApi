#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 14:00
# @Author  : Zhangyp
# @File    : zt_project.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_project_model import ProjectModel
from mid_process.request_parse import project_args
from mid_process.data_fields import project_fields
from mid_process.response_json import response


class Project(Resource):
	@staticmethod
	def post():
		body = project_args()
		project = ProjectModel.query_checkbox(body['id'], body['project_name'], body['PM'], body['product'],
											  body['team_members'])
		if project:
			data = marshal(project, project_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")
