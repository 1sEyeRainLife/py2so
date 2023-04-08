FROM python:latest

RUN mkdir /webapp

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com flask

COPY webapp webapp

WORKDIR /webapp
CMD ["python", "main.py"]