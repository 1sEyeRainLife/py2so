FROM python:latest

# RUN apt-get install gcc

RUN mkdir /webtmp && mkdir /webapp

COPY . /webtmp
WORKDIR /webtmp

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com -r requirements.txt

RUN python py2so.py --build_dir=./example/projects/src

COPY build/ /webapp/
COPY example/projects/main.py /webapp/

RUN rm -rf /webtmp
RUN rm -rf /webapp/tmp

WORKDIR /webapp
CMD ["python", "main.py"]