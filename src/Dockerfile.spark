FROM bitnami/spark:latest

COPY requirements.txt .

USER root

RUN apt-get clean  && \
	apt-get update && \
	apt-get install -y python3-pip && \
	pip3 install -r ./requirements.txt