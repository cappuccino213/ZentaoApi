#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:11
# @Author  : Zhangyp
# @File    : zt_product.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, marshal
from models.zt_product_model import ProductModel
from mid_process.data_fields import product_list_fields
from mid_process.response_json import response


class Product(Resource):
	@staticmethod
	def get():
		product_list = ProductModel.query_all()
		if product_list:
			data = marshal(product_list, product_list_fields)
			return response(True, data, "获取到产品列表")
		else:
			return response(True, None, "未获取到产品列表")
	
	@staticmethod
	def post():  # 单选查询产品
		pass
