#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 15:10
# @Author  : Zhangyp
# @File    : zt_test_story.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from flask_restful import Resource, marshal
from models.zt_story_model import StoryModel
from models.zt_action_model import ActionModel
from mid_process.request_parse import test_story_args
from mid_process.data_fields import story_fields
from mid_process.response_json import response


class TestStory(Resource):
	@staticmethod
	def post():
		body = test_story_args()
		actions = ActionModel.query_story_extra(body['user'], body['beginDate'], body['endDate'])
		story_ids = [action.objectID for action in actions]
		test_story = StoryModel.query_by_id(story_ids)
		if test_story:
			data = marshal(test_story, story_fields)
			return response(True, data, "查询到用户数据")
		else:
			return response(True, None, "未查询到用户数据")