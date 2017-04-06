FROM python:3-alpine
MAINTAINER Mostafa Razavi
WORKDIR /root
ADD templates /root/templates
ADD web.py /root
ADD requirements.txt /root
RUN pip install -r requirements.txt
CMD gunicorn web:app -b 0.0.0.0:8000
EXPOSE 8000