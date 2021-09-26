from flask_restful import Api
from db import app

# 导入资源
from resources.zt_login import Login
from resources.zt_user import User, UserList
from resources.zt_product import Product
from resources.zt_testtask import TestTask
from resources.qa_user import QaUser
from resources.qa_tasktype import QaTaskType
from resources.qa_task import QaTask
from resources.qa_testtask import QaTestTask
from resources.zt_story import Story
from resources.zt_test_story import TestStory
from resources.zt_task import Task
from resources.zt_build import BuildInfo
from resources.zt_bug import Bug
from resources.zt_project import Project
from resources.zt_project_statistics import ProjectStatistics

from resources.qa_delay_statistics import QADelayStatistics
from resources.qa_bug_severity_rate_statistics import QABugSeverityRateStatistics
from resources.qa_bug_invalid_rate_statistics import QABugInvalidRateStatistics

api = Api(app)

api.add_resource(Login, '/zentao/login')
api.add_resource(User, '/zentao/user', '/qms/user')  # /qms/user给QA系统用
api.add_resource(QaUser, '/zentao/qa_user')  # /qms/user给QA系统用
api.add_resource(UserList, '/zentao/userlist')
api.add_resource(Product, '/zentao/product')
api.add_resource(TestTask, '/zentao/testtask')
api.add_resource(Story, '/zentao/story')
api.add_resource(TestStory, '/zentao/teststory')
api.add_resource(Task, '/zentao/task')
api.add_resource(BuildInfo, '/zentao/build')
api.add_resource(Bug, '/zentao/bug')
api.add_resource(Project, '/zentao/project')
api.add_resource(ProjectStatistics, '/zentao/project_statistics')

api.add_resource(QADelayStatistics, '/zentao/qa_delay_statistics')
api.add_resource(QABugSeverityRateStatistics, '/zentao/qa_severity_statistics')
api.add_resource(QABugInvalidRateStatistics, '/zentao/qa_invalid_statistics')

api.add_resource(QaTaskType, '/qms/tasktype')
api.add_resource(QaTask, '/qms/task')
api.add_resource(QaTestTask, '/qms/testtask')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8089, threaded=True)  # processes 进程参数
