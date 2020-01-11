from django.shortcuts import render

import redis
import json
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from spider.mian import start_spider

import smtplib
from email.mime.text import MIMEText






def spider(request):

    start_spider.delay(10)

    return HttpResponse("pachong")

