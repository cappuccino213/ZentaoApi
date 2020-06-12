#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 9:24
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : wr_task_model.py
# @Software: PyCharm
from db import db


class TaskModel(db.Model):
    __bind_key__ = 'qms'
    __tablename__ = 'qa_task'

    task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_type = db.Column(db.Enum('功能测试','性能测试','接口测试','其他非功能性测试','需求确认','需求评审','技术支持','自动化测试开发'))
    product = db.Column(db.Integer)
    project = db.Column(db.Integer)
    story = db.Column(db.Integer)
    testtask = db.Column(db.Integer)
    report = db.Column(db.Integer)
    name = db.Column(db.String(128))
    desc = db.Column(db.String(1024))
    create_time = db.Column(db.DateTime)
    create_man = db.Column(db.String(16))
    plan_startdate = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    assigned_to = db.Column(db.String(16))
    start_date = db.Column(db.DateTime)
    finished_date = db.Column(db.DateTime)
    finished_man = db.Column(db.String(16))
    cancel_time = db.Column(db.DateTime)
    cancel_man = db.Column(db.String(16))
    revised_time = db.Column(db.DateTime)
    revised_man = db.Column(db.String(16))
    status = db.Column(db.Enum('wait','doing','pause','done','cancel'))
    story_url = db.Column(db.String(255))
    testtask_url = db.Column(db.String(255))
    report_url = db.Column(db.String(255))

    def __init__(self,task_type,product,project,story,testtask,report,name,desc,create_time,create_man,plan_startdate,deadline,assigned_to,start_date,finished_date,
                 finished_man,cancel_time,cancel_man,revised_time,revised_man,status,story_url,testtask_url,report_url):
        self.task_type = task_type
        self.product = product
        self.project = project
        self.story = story
        self.testtask = testtask
        self.report = report
        self.name = name
        self.desc = desc
        self.create_time = create_time
        self.create_man = create_man
        self.plan_startdate = plan_startdate
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.start_date = start_date
        self.finished_date = finished_date
        self.finished_man = finished_man
        self.cancel_time = cancel_time
        self.cancel_man = cancel_man
        self.revised_time = revised_time
        self.revised_man = revised_man
        self.status = status
        self.story_url = story_url
        self.testtask_url = testtask_url
        self.report_url = report_url

    # 获取所有未取消产品列表
    @classmethod
    def query_all(cls):
        return cls.query.filter(TaskModel.status!= 'cancel').all()

    #根据id获取任务记录
    def query_task_id(id):
        return TaskModel.query.filter(TaskModel.task_id==id).first()

    #提交到数据库
    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    def commit(self):
        db.session.commit()

#按条件查询方法（支持多选）
    @classmethod
    def query_data(cls,product,project,task_type,plan_startdate):
        filter = []
        if (product) :
            filter.append(TaskModel.product.in_(product))
        if (project) :
            filter.append(TaskModel.project.in_(project))
        if (task_type) :
            filter.append(TaskModel.task_type.in_(task_type))
        if (plan_startdate) :
            filter.append(TaskModel.plan_startdate>=plan_startdate[0])
            filter.append(TaskModel.plan_startdate <= plan_startdate[1])
        data = TaskModel.query.filter(TaskModel.status !='cancel').filter(*filter).all()
        return data