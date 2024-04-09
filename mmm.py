import json
import requests
import random
def otp():
    num=random.randint(1000,9999)
    return str(num)
def sms(phn,messege):
    url='https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization':'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id':'FSTSMS',
        'message':messege,
        'language':'english',
        'route':'q',
        'numbers':phn
    }
    requests.get(url,params)
msg=f"OTP is{otp()}"
print(msg)
sms("9531670207","Your OTP for verification is")