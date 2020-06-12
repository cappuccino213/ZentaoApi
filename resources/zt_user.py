#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 14:16
# @Author  : Zhangyp
# @File    : zt_user.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, marshal
from models.zt_user_model import UserModel
from mid_process.request_parse import user_args, user_args_list, pageinfo_args
from mid_process.data_fields import user_fields, user_list_fields, page_fields
from mid_process.response_json import response, response_pf, page_info


class User(Resource):
	@staticmethod
	def get():
		# user_qa_list = UserModel.query_QA_all() # 获取测试组用户列表
		user_qa_list = UserModel.query_all()
		if user_qa_list:
			data = marshal(user_qa_list, user_list_fields)
			return response(True, data, "获取到用户列表")
		else:
			return response(True, None, "未获取用户列表")
	
	@staticmethod
	def post():
		body = user_args()
		user = UserModel.query_conditions(body['id'], body['dept'], body['account'], body['role'], body['realname'],
										  body['gender'])
		if user:
			data = marshal(user, user_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")


class UserList(Resource):
	@staticmethod
	def post():
		users_args = user_args_list()  # 用户参数
		page_args = pageinfo_args()  # 页面参数
		users = UserModel.query_checkbox(users_args['dept'], users_args['role'], users_args['gender'],
										 page_args['pageIndex'], page_args['pageSize'])
		if users:
			data = marshal(users.items, user_fields)  # 将输用户列表内容格式化
			page_data = marshal(page_info(users.total, users.page, users.per_page), page_fields)  # 页面信息赋值且格式化
			return response_pf(True, data, page_data, "查询到用户数据")
		else:
			return response_pf(True, None, None, "未查询到用户数据")
