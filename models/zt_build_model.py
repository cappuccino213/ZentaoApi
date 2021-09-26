"""
@File : zt_build_model.py
@Date : 2021/9/26 15:46
@Author: 九层风（YePing Zhang）
@Contact : yeahcheung213@163.com
"""
from db import db


class BuildModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_build'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))
	branch = db.Column(db.Integer)
	product = db.Column(db.Integer)
	project = db.Column(db.Integer)
	scmPath = db.Column(db.String(255))
	filePath = db.Column(db.String(255))
	date = db.Column(db.Date)
	stories = db.Column(db.Text)
	bugs = db.Column(db.Text)
	builder = db.Column(db.String(30))
	desc = db.Column(db.Text)
	deleted = db.Column(db.Enum('0', '1'))

	# 通过id获取版本信息
	@classmethod
	def query_by_id(cls, _id):
		return cls.query.filter_by(id=_id, deleted='0').first()


if __name__ == "__main__":
	pass
