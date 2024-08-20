FROM --platform=linux/amd64 apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
RUN pip install praw
RUN pip install boto3
RUN pip install s3fs
RUN pip install awscli