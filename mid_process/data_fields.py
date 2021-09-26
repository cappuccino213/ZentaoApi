#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 17:51
# @Author  : Zhangyp
# @File    : data_fields.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import fields

"""输出字段的处理"""

"""页面信息"""
page_fields = {
	'pageIndex': fields.Integer,
	'pageSize': fields.Integer,
	'Count': fields.Integer
}

"""用户"""
# 用户查询输出
user_fields = {
	'id': fields.Integer,
	'dept': fields.Integer,
	'account': fields.String,
	'password': fields.String,
	'role': fields.String,
	'realname': fields.String,
	'nickname': fields.String,
	'gender': fields.String,
	'mobile': fields.String,
	'email': fields.String,
	'qq': fields.String,
	'address': fields.String,
	'deleted': fields.String
}

# 用户列表
user_list_fields = {
	'id': fields.Integer,
	'account': fields.String,
	'realname': fields.String,
	'password': fields.String
}

"""产品"""
# 产品列表
product_list_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'code': fields.String,
	'status': fields.String,
	'desc': fields.String,
	'PO': fields.String
}

"""测试单"""

testtask_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'product': fields.Integer,
	'project': fields.Integer,
	'build': fields.String,
	'owner': fields.String,
	'begin': fields.String,
	'end': fields.String,
	'status': fields.String
}

"""任务类型"""

tasktype_fields = {
	"id": fields.Integer,
	"type": fields.String
}

"""任务"""
# 任务列表
Task_list_fields = {
	'task_id': fields.Integer,
	'parent': fields.Integer,
	'task_type': fields.String,
	'product': fields.Integer,
	'product_name': fields.String,
	'project': fields.Integer,
	'project_name': fields.String,
	'story': fields.Integer,
	'story_name': fields.String,
	'testtask': fields.Integer,
	'report': fields.Integer,
	'name': fields.String,
	'desc': fields.String,
	'create_time': fields.DateTime,
	'create_man': fields.String,
	'plan_startdate': fields.DateTime,
	'deadline': fields.DateTime,
	'assigned_to': fields.String,
	'start_date': fields.DateTime,
	'finished_date': fields.DateTime,
	'finished_man': fields.String,
	'cancel_time': fields.DateTime,
	'cancel_man': fields.String,
	'revised_time': fields.DateTime,
	'revised_man': fields.String,
	'status': fields.String,
	'story_url': fields.String,
	'testtask_url': fields.String,
	'report_url': fields.String,
}

"""版本信息"""
build_info_fields = {
	'build_id': fields.Integer,
	'name': fields.String,
	'branch': fields.String,
	'product': fields.Integer,
	'project': fields.Integer,
	'scmPath': fields.String,
	'filePath': fields.String,
	'date': fields.String,
	'stories': fields.String,
	'bugs': fields.String,
	'builder': fields.String,
	'desc': fields.String
}

"""需求"""
story_fields = {
	'id': fields.Integer,
	'product': fields.Integer,
	'title': fields.String,
	'type': fields.String,
	'pri': fields.Integer,
	'status': fields.String,
	'stage': fields.String,
	'openedBy': fields.String,
	'openedDate': fields.String,
	'assignedTo': fields.String,
	'assignedDate': fields.String,
	'reviewedBy': fields.String,
	'reviewedDate': fields.String,
	'version': fields.Integer,
	'closedBy': fields.String,
	'closedDate': fields.String
}

"""任务"""
task_fields = {
	'id': fields.Integer,
	'parent': fields.Integer,
	'parentName': fields.String,
	'project': fields.Integer,
	'name': fields.String,
	'desc': fields.String,
	'type': fields.String,
	'pri': fields.Integer,
	'deadline': fields.String,
	'status': fields.String,
	'openedBy': fields.String,
	'openedDate': fields.String,
	'assignedTo': fields.String,
	'assignedDate': fields.String,
	'finishedBy': fields.String,
	'finishedDate': fields.String,
	'estStarted': fields.String,
	'realStarted': fields.String
}

"""bug"""
bug_fields = {
	'id': fields.Integer,
	'product': fields.Integer,
	'project': fields.Integer,
	'task': fields.Integer,
	'severity': fields.Integer,
	'pri': fields.Integer,
	'type': fields.String,
	'title': fields.String,
	'deadline': fields.String,
	'status': fields.String,
	'openedBy': fields.String,
	'openedDate': fields.String,
	'assignedTo': fields.String,
	'assignedDate': fields.String,
	'closedBy': fields.String,
	'closedDate': fields.String,
	'testtask': fields.String,
	'resolvedBy': fields.String,
	'resolution': fields.String,
	'resolvedBuild': fields.String,
	'resolvedDate': fields.String
}

"""project_statistic"""
project_statistics_fields = {
	'project': fields.Integer,
	'assignedTo': fields.String,
	'estimate': fields.Float,
	'consumed': fields.Float,
	'left': fields.Float
}

"""project"""
project_fields = {
	'id': fields.Integer,
	'project_name': fields.String,
	'PM': fields.String,
	'product': fields.Integer,
	'team_members': fields.String
}
