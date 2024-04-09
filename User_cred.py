import json
import random
import requests
import smtplib as s
obs = s.SMTP("smtp.gmail.com", 587)
obs.starttls()
obs.login("uddalakmukhopadhyay@gmail.com","Uddalak2005")
#########################################################################
def sms(phn,ot):
    text="Your OTP for verification is"+ ot+ ".\nDonot Share it with anyone !"
    url='https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization':'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id':'FSTSMS',
        'message':text,
        'language':'english',
        'route':'q',
        'numbers':phn
    }
    requests.get(url,params)
#####################################################################################
def response_sms(phn,text):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization': 'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id': 'FSTSMS',
        'message': text,
        'language': 'english',
        'route': 'q',
        'numbers': phn
    }
    requests.get(url, params)
##########################################################################
def response_email(address,text):
    subject = "Horizon Bank of India"
    messege="Subject:{}\n\n{}".format(subject,text)
    ob.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
##########################################################################
def email(address,code):
    global ob
    subject = "Horizon Bank of India"
    body="Your OTP for verification is "+str(code)+".\nDon't Share it with anyone"
    messege="Subject:{}\n\n{}".format(subject,body)
    ob.sendmail("uddalakmukhopadhyay@gamil.com",address,messege)
def write_json(data,filename="user_det.json"):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
with open("user_det.json",) as js:
    data=json.load(js)


def otp_gen():
    global otp_n
    otp_n = random.randint(1000, 9999)

def acc_n_sms(acc,usr,nm):
    phn="9531670207"
    text = "The user with account number - " + acc + ".\nAnd User ID - "+usr+"\nName - "+nm+"\nHave requested for a change in his account number"
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization': 'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id': 'FSTSMS',
        'message': text,
        'language': 'english',
        'route': 'q',
        'numbers': phn
    }
    requests.get(url, params)
def acc_n_email(acc,usr,nm,snd):
    address="uddalakmukhopadhyay@yahoo.com"
    text = "The user with account number - " + acc + ".\nAnd User ID - " + usr + "\nName - " + nm + "\nHave requested for a change in his/her account number"
    subject = "Horizon Bank of India"
    messege = "Subject:{}\n\n{}".format(subject, text)
    ob.sendmail(snd, address, messege)

def change(choise,acc):
    otp_gen()
    dt = data[acc]
    while choise != "1" and choise!="2":
        choise=input("Please enter a valid choise")
    if choise=="1":
        print("It seems that you have forgot your user name")
        print("-"*50)
        print("Enter (1) to reset user name through password.\nEnter (2) to reset user name through OTP")
        ch=input("Please enter your choice : ")
        while ch !="1" and ch !="2" :
            ch=input("Please enter a valid choice : ")
        if ch=="1":
            ac=input("Please enter your account number : ")
            while ac != acc:
                ac=input("The account number was wrong.\nPlease enter a valid account number : ")
            pas=input("Please enter your password: ")
            while pas != dt[0]['password']:
                pas=input("The password you entered was wrong !\nPlease enter a valid password : ")
            usr=input("Your user name should consist of 8-20 chaacters.\nPlease enter your new user name :")
            while len(usr)<8 and len(usr)>20:
                print("Your user name should consist of 8-20 characters")
                usr=input("Please enter your user name : ")
            usr1=input("Please re-enter your new user name : ")
            while usr1 != usr:
                print("There is a mistmatch !")
                usr1=input("Please re-enter your new user name : ")
            dt[0]['user_id']=usr
            write_json(data)
            print("Your User name was changed successfully!")
        if ch=="2":
            ac = input("Please enter your account number : ")
            while ac != acc:
                ac = input("The account number was wrong.\nPlease enter a valid account number : ")
            phn=dt[0]['phone']
            eml=dt[0]['email']
            #sms(phn,otp_n)
            email(eml,otp_n)
            ot=input("Please enter the OTP send to your registered mobile number or email address : ")
            while ot != otp_n :
                otp=input("Please enter a valid OTP : ")
            usr = input("Your user name should consist of 8-20 chaacters.\nPlease enter your new user name :")
            while len(usr) < 8 and len(usr) > 20:
                print("Your user name should consist of 8-20 characters")
                usr = input("Please enter your user name : ")
            usr1 = input("Please re-enter your new user name : ")
            while usr1 != usr:
                print("There is a mistmatch !")
                usr1 = input("Please re-enter your new user name : ")
            dt[0]['user_id'] = usr
            write_json(data)
            print("Your User name was changed successfully!")
        txt = "This is to inform you sir, that the user ID for your account\nhave been succesfully changed.Your new User ID is - " + dt[0]['user_id'] + "\n\nThank you,\nHorizon Bank"
    if choise=="2":
        print("It seems that you have forgot your passward")
        print("-" * 50)
        print("Enter (1) to reset user name through user name.\nEnter (2) to reset user name through OTP")
        ch = input("Please enter your choice : ")
        while ch !="1" or ch !="2" :
            ch=input("Please enter a valid choice : ")
        if ch=="1":
            ac=input("Please enter your account number : ")
            while ac != acc:
                ac=input("The account number was wrong.\nPlease enter a valid account number : ")
            pas=input("Please enter your user name: ")
            while pas != dt[0]['user_det']:
                pas=input("The password you entered was wrong !\nPlease enter a valid password : ")
            usr=input("Your passward name should consist of 8-20 chaacters.\nPlease enter your new passward :")
            while len(usr)<8 and len(usr)>20:
                print("Your passward should consist of 8-20 characters")
                usr=input("Please enter your passward name: ")
            usr1 = input("Please re-enter your new passward : ")
            while usr1 != usr:
                print("There is a mistmatch !")
                usr1 = input("Please re-enter your new passward : ")
            dt[0]['password'] = usr
            write_json(data)
            print("Your passward was changed successfully!")
        if ch=="2":
            ac = input("Please enter your account number : ")
            while ac != acc:
                ac = input("The account number was wrong.\nPlease enter a valid account number : ")
            phn=dt[0]['phone']
            eml=dt[0]['email']
            #sms(phn,otp_n)
            email(eml,otp_n)
            ot=input("Please enter the OTP send to your registered mobile number or email address : ")
            while ot != otp_n :
                otp=input("Please enter a valid OTP : ")
            usr = input("Your passward should consist of 8-20 chaacters.\nPlease enter your new passward :")
            while len(usr) < 8 and len(usr) > 20:
                print("Your passward should consist of 8-20 characters")
                usr = input("Please enter your passward : ")
            usr1 = input("Please re-enter your new passward : ")
            while usr1 != usr:
                print("There is a mistmatch !")
                usr1 = input("Please re-enter your new passward : ")
            dt[0]['user_id'] = usr
            write_json(data)
            print("Your passward was changed successfully!")
        txt="This is to inform you sir, that the password for your account\nhave been succesfully changed.Your new passward is - "+dt[0]['password']+"\n\nThank you,\nHorizon Bank"
        phn=dt[0]['phone']
        eml=dt[0]['email']
        #response_sms(phn,txt)
        response_email(eml,txt)
    if choise=="3":
        nm=dt[0]['name']
        usr=dt[0]['user_id']
        eml=dt[0]['email']
        #acc_n_sms(acc,usr,nm)
        acc_n_email(acc,usr,nm,eml)
        print("Your request for a change in user name have been successfully submitted !")