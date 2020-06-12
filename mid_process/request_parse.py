#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 17:44
# @Author  : Zhangyp
# @File    : request_parse.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import reqparse

"""页面信息入参"""


def pageinfo_args():
	args = reqparse.RequestParser()
	args.add_argument('pageIndex', type=int, default=1, help="page must be a positive integer")
	args.add_argument('pageSize', type=int, default=10, help="per_page must be a positive integer")
	return args.parse_args()


"""登录接口入参解析"""


def login_args():
	args = reqparse.RequestParser()
	args.add_argument('account', type=str)
	args.add_argument('password', type=str)
	return args.parse_args()


"""用户查询入参解析"""


# 单选条件查询
def user_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int)
	args.add_argument('dept', type=str)
	args.add_argument('account', type=str)
	args.add_argument('role', type=str)
	args.add_argument('realname', type=str)
	args.add_argument('gender', type=str)
	return args.parse_args()


# 多选条件查询
def user_args_list():
	args = reqparse.RequestParser()
	args.add_argument('dept', type=int, action='append')
	args.add_argument('role', type=str, action='append')
	args.add_argument('gender', type=str, action='append')
	return args.parse_args()


"""测试单入参解析"""


# id获取
def testtask_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int)
	return args.parse_args()


"""新增任务入参解析"""


# 插入任务
def qa_task_args():
	args = reqparse.RequestParser()
	args.add_argument('task_type', type=str)
	args.add_argument('product', type=int)
	args.add_argument('project', type=int)
	args.add_argument('story', type=int)
	args.add_argument('testtask', type=int)
	args.add_argument('report', type=int)
	args.add_argument('name', type=str)
	args.add_argument('desc', type=str)
	args.add_argument('create_time', type=str)
	args.add_argument('create_man', type=str)
	args.add_argument('plan_startdate', type=str)
	args.add_argument('deadline', type=str)
	args.add_argument('assigned_to', type=str)
	args.add_argument('start_date', type=str)
	args.add_argument('finished_date', type=str)
	args.add_argument('finished_man', type=str)
	args.add_argument('cancel_time', type=str)
	args.add_argument('cancel_man', type=str)
	args.add_argument('revised_time', type=str)
	args.add_argument('revised_man', type=str)
	args.add_argument('status', type=str)
	args.add_argument('story_url', type=str)
	args.add_argument('testtask_url', type=str)
	args.add_argument('report_url', type=str)
	return args.parse_args()


"""新增冒烟测试入参解析"""


# 插入冒烟测试任务
def qa_testtask_args():
	args = reqparse.RequestParser()
	args.add_argument('name', type=str)
	args.add_argument('product', type=int)
	args.add_argument('project', type=str)
	args.add_argument('build_man', type=str)
	args.add_argument('owner', type=str)
	args.add_argument('smokeresult', type=int)
	args.add_argument('reason', type=str)
	args.add_argument('desc', type=str)
	args.add_argument('perpetrators', type=str)
	args.add_argument('tester', type=str)
	args.add_argument('starttime', type=str)
	args.add_argument('finishedtime', type=str)
	return args.parse_args()


"""需求查询"""


def story_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int, action='append')
	args.add_argument('product', type=int, action='append')
	args.add_argument('openedBy', type=str, action='append')
	args.add_argument('assignedTo', type=str, action='append')
	args.add_argument('reviewedBy', type=str, action='append')
	args.add_argument('dateType', type=str)
	args.add_argument('beginDate', type=str)
	args.add_argument('endDate', type=str)
	args.add_argument('status', type=str, action='append')
	return args.parse_args()


"""任务查询"""


def task_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int, action='append')
	args.add_argument('openedBy', type=str, action='append')
	args.add_argument('assignedTo', type=str, action='append')
	args.add_argument('finishedBy', type=str, action='append')
	args.add_argument('dateType', type=str)
	args.add_argument('beginDate', type=str)
	args.add_argument('endDate', type=str)
	args.add_argument('project', type=str, action='append')
	args.add_argument('status', type=str, action='append')
	return args.parse_args()


"""bug查询"""


def bug_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int, action='append')
	args.add_argument('product', type=int, action='append')
	args.add_argument('project', type=int, action='append')
	args.add_argument('severity', type=int, action='append')
	args.add_argument('openedBy', type=str, action='append')
	args.add_argument('assignedTo', type=str, action='append')
	args.add_argument('closedBy', type=str, action='append')
	args.add_argument('resolvedBy', type=str, action='append')
	args.add_argument('dateType', type=str)
	args.add_argument('beginDate', type=str)
	args.add_argument('endDate', type=str)
	args.add_argument('status', type=str, action='append')
	return args.parse_args()


"""test_story查询"""


def test_story_args():
	args = reqparse.RequestParser()
	args.add_argument('user', type=str)
	args.add_argument('beginDate', type=str)
	args.add_argument('endDate', type=str)
	return args.parse_args()


"""project_statistics查询"""


def project_statistics_args():
	args = reqparse.RequestParser()
	args.add_argument('project', type=int, action='append')
	args.add_argument('assignedTo', type=str, action='append')
	return args.parse_args()


"""project查询"""


def project_args():
	args = reqparse.RequestParser()
	args.add_argument('id', type=int, action='append')
	args.add_argument('project_name', type=str, action='append')
	args.add_argument('PM', type=str, action='append')
	args.add_argument('product', type=int, action='append')
	args.add_argument('team_members', type=str)
	return args.parse_args()


"""测试考核统计--测试延期统计"""


def qa_delay_args():
	args = reqparse.RequestParser()
	args.add_argument('begin', type=str)
	args.add_argument('end', type=str)
	args.add_argument('account', type=str, action='append')
	return args.parse_args()


"""测试考核统计--bug严重率、bug有效率统计"""


def qa_bug_statistics_args():
	args = reqparse.RequestParser()
	args.add_argument('begin', type=str)
	args.add_argument('end', type=str)
	return args.parse_args()
