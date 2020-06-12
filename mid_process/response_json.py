#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 10:10
# @Author  : Zhangyp
# @File    : response_json.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask import jsonify


# 页面信息
def page_info(count, page_index, page_size):
	return {'Count': count, 'pageIndex': page_index, 'pageSize': page_size}


# 默认返回数据格式
def response(status, data, msg):
	return jsonify({
		"status": status,
		"data": data,
		"msg": msg
	})


# 分页返回数据，给页面显示用
def response_pf(status, data, page_info, msg):
	return jsonify({
		"status": status,
		"data": data,
		"pageInfo": page_info,
		"msg": msg
	})
