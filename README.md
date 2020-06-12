# ZentaoApi
基于禅道数据库（开源12.3）的禅道API接口

1框架
flask—restful+flask-sqlalchemy（orm）+python3.7

2项目结构
2.1package
mid_process：中间的数据处理方法
models：orm数据建模
resource：各数据资源的接口定义
2.2py
app.py:主程序
db.py:应用程序+数据实例化
config.py：程序相关配置
