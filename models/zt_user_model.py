#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 16:21
# @Author  : Zhangyp
# @File    : zt_user_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db import db
import hashlib


class UserModel(db.Model):
	__bind_key__ = 'zentao'
	__tablename__ = 'zt_user'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	dept = db.Column(db.Integer)
	account = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(32))
	role = db.Column(db.String(10))
	realname = db.Column(db.String(100))
	nickname = db.Column(db.String(60))
	gender = db.Column(db.Enum('f', 'm'))
	mobile = db.Column(db.String(11))
	email = db.Column(db.String(90))
	qq = db.Column(db.String(20))
	address = db.Column(db.String(120))
	deleted = db.Column(db.Enum('0', '1'))
	
	def __init__(self, _id, dept, account, password, role, realname, nickname, gender, deleted):
		self.id = _id
		self.dept = dept
		self.account = account
		self.password = password
		self.role = role
		self.realname = realname
		self.nickname = nickname
		self.gender = gender
		self.deleted = deleted
	
	# 验证密码是否匹配
	def check_password(self, type_pwd):
		cipher_obj = hashlib.md5(type_pwd.encode('utf-8'))  # 传入值md5后验证数据库密码
		cipher_str = cipher_obj.hexdigest()
		if self.password == cipher_str:
			return True
		else:
			return False
	
	# 查询是否存在账号
	@classmethod
	def query_by_account(cls, acc):
		try:
			result = cls.query.filter_by(account=acc, deleted='0').first()
		except:
			result = None
		return result
	
	@classmethod
	def query_QA_all(cls):
		result = cls.query.filter_by(dept='4', deleted='0').all()
		return result
	
	@classmethod
	def query_all(cls):
		result = cls.query.filter_by(deleted='0').all()
		# result = cls.query.filter(UserModel.dept != '5', UserModel.deleted == '0').all()  # 筛选掉工程部门的用户
		return result
	
	# 根据单选条件查询
	@classmethod
	def query_conditions(cls, _id, dept, account, role, realname, gender):
		result = cls.query.filter_by(deleted='0')
		if _id:
			result = result.filter_by(id=_id)
		if dept:
			result = result.filter_by(dept=dept)
		if account:
			result = result.filter_by(account=account)
		if role:
			result = result.filter_by(role=role)
		if realname:
			result = result.filter_by(realname=realname)
		if gender:
			result = result.filter_by(gender=gender)
		return result.all()
	
	# 多选条件查询(一般字段是枚举类型会多选)
	@classmethod
	def query_checkbox(cls, dept_list, role_list, gender_list, page_index=1, page_size=10):  # 默认第一页，10条/页
		result = cls.query.filter_by(deleted='0')
		if dept_list:
			result = result.filter(cls.dept.in_(dept_list))
		if role_list:
			result = result.filter(cls.role.in_(role_list))
		if gender_list:
			result = result.filter(cls.gender.in_(gender_list))
		return result.paginate(page=page_index, per_page=page_size)


if __name__ == '__main__':
	u = UserModel
	r = u.query_conditions('3', '', 'zyp', '', '', '')
	r1 = u.query_by_account('zyp')
	print(type(r))
	print(type(r1))
