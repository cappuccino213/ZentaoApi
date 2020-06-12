#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 16:02
# @Author  : Zhangyp
# @File    : qa_user.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

# """重定向示例"""
# from flask_restful import Resource
# from flask_restful import url_for
# from flask import redirect
#
#
# class QaUser(Resource):
# 	@staticmethod
# 	def get():
# 		return redirect(url_for('/zentao/user'))

from flask_restful import Resource, marshal
from models.zt_user_model import UserModel
from mid_process.data_fields import user_list_fields
from mid_process.response_json import response


class QaUser(Resource):
	@staticmethod
	def get():
		user_qa_list = UserModel.query_QA_all()  # 获取测试组用户列表
		if user_qa_list:
			data = marshal(user_qa_list, user_list_fields)
			return response(True, data, "获取到用户列表")
		else:
			return response(True, None, "未获取用户列表")
