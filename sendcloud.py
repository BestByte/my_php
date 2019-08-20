#!/usr/bin/python
#coding:utf-8
import requests
import json

url = "http://api.sendcloud.net/apiv2/mail/send"

# 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
params = {"apiUser": "askhub",
          "apiKey": "XAvKyQbdoMZAyCnr",
          "from": "info@askhub.cc",
          "fromName": "askhub测试邮件",
          "to": "a1564987571@gmail.com",
          "subject": "来自askhub的第一封邮件！",
          "html": "你太棒了！你已成功的从askhub发送了一封测试邮件，接下来快登录前台去完善账户信息吧！",
          }

r = requests.post(url, files={}, data=params)
#print(r.text)
