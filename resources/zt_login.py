#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 16:21
# @Author  : Zhangyp
# @File    : zt_login.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, marshal
from models.zt_user_model import UserModel
from mid_process.request_parse import login_args
from mid_process.data_fields import user_fields
from mid_process.response_json import response


class Login(Resource):
	@staticmethod
	def post():
		body = login_args()
		user = UserModel.query_by_account(body['account'])
		if user:
			if user.check_password(body['password']):
				data = marshal(user, user_fields)
				return response(True, data, "登录成功")
			else:
				return response(True, None, "账号或密码错误")
		else:
			return response(True, None, "账号或密码错误")
		