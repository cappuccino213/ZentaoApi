#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 18:03
# @Author  : Zhangyp
# @File    : zt_project_statistics.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_project_statistics_model import ZtProjectStatisticsModel
from mid_process.request_parse import project_statistics_args
from mid_process.data_fields import project_statistics_fields
from mid_process.response_json import response


class ProjectStatistics(Resource):
	@staticmethod
	def post():
		body = project_statistics_args()
		project_statistics = ZtProjectStatisticsModel.query_checkbox(body['project'],body['assignedTo'])
		if project_statistics:
			data = marshal(project_statistics, project_statistics_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")