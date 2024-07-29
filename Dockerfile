FROM python:3.9.6-slim
LABEL authors="zhangyp"

# 开放端口
EXPOSE 8089

# 避免生成.pyc文件
ENV PYTHONDONTWRITEBYTECODE=1

# 关闭输出缓冲，方便日志记录
ENV PYTHONUNBUFFERED=1

# 设置时区
ENV TZ=Asia/Shanghai

# 设置工作目录
WORKDIR /zentao_api

# 复制程序相关文件 （第一个表示当前路径，第二表示容器路径）
COPY requirements.txt /zentao_api/
COPY . /zentao_api

# 使用阿里云镜像加速依赖下载，同时确保安装过程的错误能被捕获
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && echo "Dependencies installed successfully."

# 指定容器启动时的命令
CMD ["python", "./app.py"]