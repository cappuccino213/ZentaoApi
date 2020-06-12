#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 16:27
# @Author  : Zhangyp
# @File    : db.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
