# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /omi_telebot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
