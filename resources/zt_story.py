#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 10:31
# @Author  : Zhangyp
# @File    : zt_story.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_story_model import StoryModel
from mid_process.request_parse import story_args
from mid_process.data_fields import story_fields
from mid_process.response_json import response


class Story(Resource):
	@staticmethod
	def post():
		body = story_args()
		story = StoryModel.query_checkbox(body['product'], body['openedBy'], body['assignedTo'], body['reviewedBy'],
										  body['dateType'], body['beginDate'], body['endDate'],body['status'])
		if story:
			data = marshal(story, story_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")
