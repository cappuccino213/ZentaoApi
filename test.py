#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 14:53
# @Author  : Zhangyp
# @File    : test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from models.zt_testtask_report_model import TestTaskReportModel
from mid_process.data_handle import parse_html,bug_severity_rate_statistics

# ttr = TestTaskReportModel()
# r = ttr.query_checkbox('2020-03-01', '2020-06-30', [])


# print(r[0].task_desc)
def task_report_statistc(_list):
	rows = []
	for row in _list:
		row_list = []
		exp_desc = parse_html(row.task_desc)
		act_desc = parse_html(row.report_desc)
		# 获取延期时间
		exp_list = exp_desc.replace(' ', '').split('M')
		if exp_list[-1] == 'H':
			exp = float(exp_list[0]) / 8
		else:
			exp = float(exp_list[0])
		act_list = act_desc.replace(' ', '').split('M')
		if act_list[-1] == 'H':
			act = float(act_list[0]) / 8
		else:
			act = float(act_list[0])
		ed = act - exp
		row_list.extend([row.task_id, row.reporter, exp_desc, act_desc, ed])
		rows.append(row_list)
	return rows
# print(task_report_statistc(r))

r1=bug_severity_rate_statistics('2020-03-01','2020-06-30')
print(r1)