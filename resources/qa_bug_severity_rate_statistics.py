#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 17:14
# @Author  : Zhangyp
# @File    : qa_bug_severity_rate_statistics.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource
from mid_process.request_parse import qa_bug_statistics_args
from mid_process.response_json import response
from mid_process.data_handle import bug_severity_rate_statistics


class QABugSeverityRateStatistics(Resource):
	@staticmethod
	def post():
		body = qa_bug_statistics_args()
		severity_rate = bug_severity_rate_statistics(body['begin'], body['end'])
		if severity_rate:
			data = severity_rate
			return response(True, data, "获取到统计信息")
		else:
			return response(True, None, "未获取统计信息")
