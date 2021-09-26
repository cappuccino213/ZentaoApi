"""
@File : zt_build.py
@Date : 2021/9/26 15:54
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from flask_restful import Resource, marshal
from models.zt_build_model import BuildModel
from mid_process.request_parse import build_info_args
from mid_process.data_fields import build_info_fields
from mid_process.response_json import response


class BuildInfo(Resource):
	@staticmethod
	def get():
		args = build_info_args()
		build_info = BuildModel.query_by_id(args['id'])
		if build_info:
			data = marshal(build_info, build_info_fields)
			return response(True, data, "获取到版本信息")
		else:
			return response(True, None, "未获版本信息")


if __name__ == "__main__":
	pass
