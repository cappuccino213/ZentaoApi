#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 15:43
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : qa_testtask.py
# @Software: PyCharm
from flask_restful import Resource, marshal
from mid_process.request_parse import qa_task_args, qa_testtask_args
from models.qa_testtask_model import TestTaskModel
from mid_process.data_fields import Task_list_fields
from mid_process.response_json import response



class QaTestTask(Resource):
    @staticmethod
    def get():
        TestTask_list = TestTaskModel.query_all()
        if TestTask_list:
            data = marshal(TestTask_list, Task_list_fields)
            return response(True, data, "获取到任务列表")
        else:
            return response(True, None, "未获取到任务列表")


    @staticmethod
    def post():
        args = qa_testtask_args()
        name = args['name']
        product = args['product']
        project = args['project']
        build_man = args['build_man']
        owner = args['owner']
        smokeresult = args['smokeresult']
        reason = args['reason']
        perpetrators = args['perpetrators']
        tester = args['tester']
        starttime = args['starttime']
        finishedtime = args['finishedtime']

        testtask = TestTaskModel(name=name,
                         product= product,
                         project=project,
                         build_man=build_man,
                         owner=owner,
                         smokeresult=smokeresult,
                         reason=reason,
                         perpetrators=perpetrators,
                         tester=tester,
                         starttime=starttime,
                         finishedtime=finishedtime,
                         )

        testtask.add_to_db()
        if (testtask.id is None):
            return ("任务插入失败")
        else:
            return ("任务新增成功")


    @staticmethod
    def put():
        args = qa_testtask_args()
        id = args['id']
        name = args['name']
        product = args['product']
        project = args['project']
        build_man = args['build_man']
        owner = args['owner']
        smokeresult = args['smokeresult']
        reason = args['reason']
        perpetrators = args['perpetrators']
        tester = args['tester']
        starttime = args['starttime']
        finishedtime = args['finishedtime']

        testtask = TestTaskModel.query_id(id)
        testtask.name = name
        testtask.product = product
        testtask.project = project
        testtask.build_man = build_man
        testtask.owner = owner
        testtask.smokeresult = smokeresult
        testtask.reason = reason
        testtask.perpetrators = perpetrators
        testtask.tester = tester
        testtask.starttime = starttime
        testtask.finishedtime = finishedtime
        TestTaskModel.commit(testtask)
        return("更新成功")

    @staticmethod
    def delete():
        args = qa_testtask_args()
        id = args['id']
        task = TestTaskModel.query_id(id)
        task.deleteflag = 1
        TestTaskModel.commit(task)
        return("冒烟任务删除成功")#后面还需增加一个更新异常的判断处理