#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 10:52
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : qa_task.py
# @Software: PyCharm
from flask_restful import Resource, marshal
from mid_process.request_parse import qa_task_args
from models.qa_task_model import TaskModel
from mid_process.data_fields import Task_list_fields
from mid_process.response_json import response


class QaTask(Resource):
    @staticmethod
    def get():
        Task_list = TaskModel.query_all()
        #添加项目名，产品名称等信息到返回列表中
        als = []
        for i in range(len(Task_list)):
            to_json = {'task_id': Task_list[i].task_id,
                       'task_type': Task_list[i].task_type,
                       'product': Task_list[i].product,
                       'product_name':None,
                       'project': Task_list[i].project,
                       'project_name':None,
                       'story': Task_list[i].story,
                       'story_name':None,
                       'testtask': Task_list[i].testtask,
                       'report': Task_list[i].report,
                       'name': Task_list[i].name,
                       'desc': Task_list[i].desc,
                       'create_time': Task_list[i].create_time,
                       'create_man': Task_list[i].create_man,
                       'plan_startdate': Task_list[i].plan_startdate,
                       'deadline': Task_list[i].deadline,
                       'assigned_to': Task_list[i].assigned_to,
                       'start_date': Task_list[i].start_date,
                       'finished_date': Task_list[i].finished_date,
                       'finished_man': Task_list[i].finished_man,
                       'cancel_time': Task_list[i].cancel_time,
                       'cancel_man': Task_list[i].cancel_man,
                       'revised_time': Task_list[i].revised_time,
                       'revised_man': Task_list[i].revised_man,
                       'status': Task_list[i].status,
                       'story_url': Task_list[i].story_url,
                       'testtask_url': Task_list[i].testtask_url,
                       'report_url': Task_list[i].report_url
                       }
            als.append(to_json)
        if als:
            data = [marshal(al, Task_list_fields) for al in als]
            return response(True, data, "获取到任务列表")
        else:
            return response(True, None, "未获取到任务列表")

    @staticmethod
    def post():
        args = qa_task_args()
        # print(args)
        task_type = args['task_type']
        product = args['product']
        project = args['project']
        story = args['story']
        testtask = args['testtask']
        report = args['report']
        name = args['name']
        desc = args['desc']
        create_time = None
        create_man = args['create_man']
        plan_startdate = args['plan_startdate']
        deadline = args['deadline']
        assigned_to = args['assigned_to']
        start_date = args['start_date']
        finished_date = None
        finished_man = args['finished_man']
        cancel_man = None
        cancel_time = None
        revised_man = args['revised_man']
        revised_time = None
        status = args['status']
        story_url = args['story_url']
        testtask_url = args['testtask_url']
        report_url = args['report_url']
        task = TaskModel(task_type=task_type,
                         product= product,
                         project=project,
                         story=story,
                         testtask=testtask,
                         report=report,
                         name=name,
                         desc=desc,
                         create_time=create_time,
                         create_man=create_man,
                         plan_startdate=plan_startdate,
                         deadline=deadline,
                         assigned_to=assigned_to,
                         start_date=start_date,
                         finished_date=finished_date,
                         finished_man=finished_man,
                         cancel_man=cancel_man,
                         cancel_time=cancel_time,
                         revised_man=revised_man,
                         revised_time=revised_time,
                         status=status,
                         story_url=story_url,
                         testtask_url=testtask_url,
                         report_url=report_url
                         )
        task.add_to_db()
        if (task.task_id is None):
            return ("任务插入失败")
        else:
            return ("任务新增成功")

    @staticmethod
    def put():
        args = qa_task_args()
        task_id = args['task_id']
        task_type = args['task_type']
        product = args['product']
        project = args['project']
        story = args['story']
        testtask = args['testtask']
        report = args['report']
        name = args['name']
        desc = args['desc']
        create_man = args['create_man']
        plan_startdate = args['plan_startdate']
        deadline = args['deadline']
        assigned_to = args['assigned_to']
        start_date = args['start_date']
        finished_man = args['finished_man']
        revised_man = args['revised_man']
        status = args['status']
        story_url = args['story_url']
        testtask_url = args['testtask_url']
        report_url = args['report_url']

        task = TaskModel.query_task_id(task_id)
        print(task)
        task.task_type = task_type
        task.product = product
        task.project = project
        task.story = story
        task.testtask = testtask
        task.report = report
        task.name = name
        task.desc = desc
        task.create_man = create_man
        task.plan_startdate = plan_startdate
        task.deadline = deadline
        task.assigned_to = assigned_to
        task.finished_man = finished_man
        task.revised_man = revised_man
        task.start_date = start_date
        task.status = status
        task.story_url = story_url
        task.testtask_url = testtask_url
        task.report_url = report_url
        TaskModel.commit(task)
        return ("任务更新成功")#后面还需增加一个插入异常的判断处理

    @staticmethod
    def delete():
        args = qa_task_args()
        task_id = args['task_id']
        task = TaskModel.query_task_id(task_id)
        task.status = 'cancel'
        TaskModel.commit(task)
        return("任务删除成功")#后面还需增加一个更新异常的判断处理


class QaQueryTask(Resource):
    @staticmethod
    def get():
        args = QaQueryTask_args()
        product = args['product']
        project = args['project']
        task_type = args['task_type']
        plan_startdate = args['plan_startdate']
        print(plan_startdate)
        Task_list = TaskModel.query_data(product,project,task_type,plan_startdate)
        #添加项目名，产品名称等信息到返回列表中
        als = []
        for i in range(len(Task_list)):
            to_json = {'task_id': Task_list[i].task_id,
                       'task_type': Task_list[i].task_type,
                       'product': Task_list[i].product,
                       'product_name':None,
                       'project': Task_list[i].project,
                       'project_name':None,
                       'story': Task_list[i].story,
                       'story_name':None,
                       'testtask': Task_list[i].testtask,
                       'report': Task_list[i].report,
                       'name': Task_list[i].name,
                       'desc': Task_list[i].desc,
                       'create_time': Task_list[i].create_time,
                       'create_man': Task_list[i].create_man,
                       'plan_startdate': Task_list[i].plan_startdate,
                       'deadline': Task_list[i].deadline,
                       'assigned_to': Task_list[i].assigned_to,
                       'start_date': Task_list[i].start_date,
                       'finished_date': Task_list[i].finished_date,
                       'finished_man': Task_list[i].finished_man,
                       'cancel_time': Task_list[i].cancel_time,
                       'cancel_man': Task_list[i].cancel_man,
                       'revised_time': Task_list[i].revised_time,
                       'revised_man': Task_list[i].revised_man,
                       'status': Task_list[i].status,
                       'story_url': Task_list[i].story_url,
                       'testtask_url': Task_list[i].testtask_url,
                       'report_url': Task_list[i].report_url
                       }
            als.append(to_json)
        if als:
            data = [marshal(al, Task_list_fields) for al in als]
            return response(True, data, "获取到任务列表")
        else:
            return response(True, None, "未获取到任务列表")