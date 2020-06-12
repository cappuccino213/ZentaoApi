#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 15:53
# @Author  : Zhangyp
# @File    : qa_delay_statistics.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource
from models.zt_testtask_report_model import TestTaskReportModel
from mid_process.request_parse import qa_delay_args
from mid_process.response_json import response
from mid_process.data_handle import task_report_statistc

class QADelayStatistics(Resource):
	@staticmethod
	def post():
		body = qa_delay_args()
		task_report = TestTaskReportModel.query_checkbox(body['begin'], body['end'],body['account'])
		if task_report:
			data = task_report_statistc(task_report)
			return response(True, data, "获取到统计信息")
		else:
			return response(True, None, "未获取统计信息")
