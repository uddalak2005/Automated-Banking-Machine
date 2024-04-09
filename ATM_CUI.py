import json
import requests
import random
import smtplib as s
import User_cred
ob = s.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login("uddalakmukhopadhyay@gmail.com","Uddalak2005")
def email(address,code):
    global ob
    subject = "Horizon Bank of India"
    body="Your one time pass word for transaction is "+str(code)+".\nDon't Share it with anyone"
    messege="Subject:{}\n\n{}".format(subject,body)
    ob.sendmail("uddalakmukhopadhyay@gamil.com",address,messege)
#################################################################################
def response_mail(address,wid,avl,acc_no):
    subject = "Transaction Report"
    st="XXXX"+acc_no[4:]
    body="This is to inform you that,\nrecent transaction of - INR "+str(wid)+"\nfrom account number - "+st+"\nAvailable amount - INR "+str(avl)+"\n\nReagrds Horizon Bank,"
    messege = "Subject:{}\n\n{}".format(subject, body)
    ob.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
########################################################################################
def trans_mail(address,wid,avl,acc_no):
    subject = "Deposition Report"
    st="XXXX"+acc_no[4:]
    body="This is to inform you that,\nrecent deposition of - INR "+str(wid)+"\nfrom account number - "+st+"\nAvailable amount -  INR "+str(avl)+"\n\nReagrds Horizon Bank,"
    messege = "Subject:{}\n\n{}".format(subject, body)
    ob.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
#########################################################################################
def new(address,acc_no,name,usr,pas,phn,amt):
    subject="Welcome to Horizon Bank of India"
    body="We are very glad to welcome our honourable customer to one of the best banks in India\nfounded by Uddalak Mukhopadhyay,that provides one of the best and exotix banking services in the sub-continue.Your credentials are as follows - \n"+"Name - "+str(name)+"\nAccount number - "+str(acc_no)+"\nUser ID - "+str(usr)+"\nPassward - "+str(pas)+"\nPhone numebr - "+str(phn)+"\nEmail ID - "+str(address)+"\nAmount deposited -  INR "+str(amt)+"\n\nThank you for choosing us"
    messege = "Subject:{}\n\n{}".format(subject, body)
    ob.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
######################################################################################
def write_json(data,filename="user_det.json"):
    with open(filename, 'w') as f:
        json.dump(data,f,indent=4)
###############################################################################
with open("user_det.json") as json_file:
    data=json.load(json_file)
otp_n=0
def otp():
    global otp_n
    otp_n=random.randint(1000,9999)
#########################################################################
def sms(phn,text):
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
##########################################################################
def response_sms(phn,wid,avl,acc_no):
    url='https://www.fast2sms.com/dev/bulkV2'
    st = "XXXX" + acc_no[4:]
    text="This is to inform you that,\nrecent transaction of - INR "+str(wid)+"\nfrom account number - "+st+"\nAvailable amount - INR "+str(avl)+"\n\nReagrds Horizon Bank,"
    params={
        'authorization':'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id':'FSTSMS',
        'message':text,
        'language':'english',
        'route':'q',
        'numbers':phn
    }
    requests.get(url,params)
#########################################################################
def trans_sms(phn,wid,avl,acc_no):
    url='https://www.fast2sms.com/dev/bulkV2'
    st = "XXXX" + acc_no[4:]
    text="This is to inform you that,\nrecent deposition of - INR "+str(wid)+"\nfrom account number - "+st+"\nAvailable amount - INR "+str(avl)+"\n\nReagrds Horizon Bank,"
    params={
        'authorization':'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id':'FSTSMS',
        'message':text,
        'language':'english',
        'route':'q',
        'numbers':phn
    }
    requests.get(url,params)
#########################################################################
def new_sms(address,acc_no,name,usr,pas,phn,amt):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    text="We are very glad to welcome our honourable customer to one of the best banks in India\nfounded by Uddalak Mukhopadhyay,that provides one of the best and exotix banking services in the sub-continue.Your credentials are as follows - \n"+"Name - "+str(name)+"\nAccount number - "+str(acc_no)+"\nUser ID - "+str(usr)+"\nPassward - "+str(pas)+"\nPhone numebr - "+str(phn)+"\nEmail ID - "+str(address)+"\nAmount deposited -  INR "+str(amt)+"\n\nThank you for choosing us"
    params = {
        'authorization': 'GJEa4qpYxbBhgong98iRTiqxW22r1W6hmKujGgkRE6Ma6AnPThxKHORbZYkh',
        'sender_id': 'FSTSMS',
        'message': text,
        'language': 'english',
        'route': 'q',
        'numbers': phn
    }
    requests.get(url, params)
#########################################################################
def account():
    num=random.randint(100000,999999)
    n=1
    while n>0:
        if num not in data:
            return num
            break
#########################################################################
#########################################################################
def bank():
    n=1
    while n>0:
        print("-"*50,"\n","-"*50)
        print("Welcome to Horizon Bank of India")
        print('-'*50)
        print("Please Enter \'0\' if you are an existing customer\nOR,Please Enter \'1\' if you are a new customer")
        inp=input("Enter your choise : ")
        if inp=='0':
            n=1
            x=1
            acc=input("Please enter your account number : ")
            while acc not in data:
                acc=input("Please enter a valid account number : ")
                print("It seems like you have forgotten your user name : ")
                User_cred.change("3")
            cust=data[acc]
            usr_id=input("Please enter for user id : ")
            while usr_id != cust[0]['user_id']:
                usr_id=input("Please enter a valid user id : ")
                if x>=4:
                    print("It seems like you have forgotten your user id: ")
                    en=input("Enter (1) to change user ID.\nEnter (2) to continue : ")
                    while en != "1" and en != "2":
                        en=input("Please enter a valid choice : ")
                    if en=="1":
                        User_cred.change("1",acc)
                x+=1
            x=1
            password=input("Please enter your password : ")
            while password != cust[0]['password']:
                password=input("Please enter a valid password : ")
                if x >= 4:
                    print("It seems like you have forgotten passward: ")
                    en = input("Enter (1) to change user ID.\nEnter (2) to continue : ")
                    while en != "1" and en != "2":
                        en = input("Please enter a valid choice : ")
                    if en == "1":
                        User_cred.change("2", acc)
                x+=1
            print("-"*50)
            print("Enter \'1\' to check your amount\nEnter \'2\' to withdrawl\nEnter \'3\' to deposit amount")
            usr_inp=input("Enter your choise : ")
            if usr_inp=='1':
                print("Your current account balance is : ",cust[0]['amount'])
            elif usr_inp=='2':
                amt = int(input("Please enter the amount to be withdrawn : "))
                paswrd = input("Please enter your passward : ")
                while paswrd != cust[0]['password']:
                    print("The passward that you entered was wrong ! ")
                    paswrd = input("Please enter a valid passward : ")
                phnum=cust[0]['phone']
                em=cust[0]['email']
                otp()

                email(em,otp_n)
                ver = input("Please Enter the OTP send on your linked mobile number or email : ")
                mesg="Your OTP  for Horizon Bank of India is "+str(otp_n)+".\nPlease don't share the OTP with anyone !"
                #sms(phnum,mesg)
                while ver != str(otp_n):
                    print("Invalid OTP !")
                    ver=input("Please enter a valid OTP : ")
                while amt > int(cust[0]['amount']):
                    print("You don't have enough money to withdraw")
                    amt=input("Please enter the amount to be withdrawn : ")
                print("Your amount have been withdrawn")
                fn=int(cust[0]['amount'])-amt
                print("Your current amount is : ",fn)
                cust[0]['amount']=fn
                write_json(data)
                response_mail(em,amt,fn,acc)
                #response_sms(phnum,amt,fn,acc)
            elif usr_inp=='3':
                amt = int(input("Enter amount to be saved : "))
                paswrd = input("Please enter your passward : ")
                while paswrd != cust[0]['password']:
                    print("The passward that you entered was wrong ! ")
                    paswrd=input("Please enter a valid passward : ")
                phnum = cust[0]['phone']
                em=cust[0]['email']
                otp()
                mesg = "Your OTP  for Horizon Bank of India is " +str(otp_n)+".\nPlease don't share the OTP with anyone !"
                #sms(phnum, mesg)
                ver = input("Please Enter the OTP send on your linked mobile number : ")
                while ver != str(otp_n):
                    print("Invalid OTP !")
                    ver = input("Please enter a valid OTP : ")
                fn=cust[0]['amount']+amt
                cust[0]['amount']=fn
                print("your current balance is : ",cust[0]['amount'])
                trans_mail(em,amt,fn,acc)
                #trans_sms(phnum,amt,fn,acc)
                write_json(data)
            else:
                print("Wrong choise !")
            print("Enter 0 to continue ; enter 1 to end")
            u=input("Enter your choise : ")
            if u=='1':
                print("Thank you for choosing us")
                break
            else:
                print("Wrong choise !")
        if inp=='1':
            n=1
            print("*"*50)
            print("Welcome to horizon bank")
            print("For registration please fill your details below")
            print("*" * 50)
            nam=input("Enter your name : ")
            print("-"*50)
            print("your user id must be  of 8-20 characters")
            id=input("Create your user id : ")
            while n > 0:
                if len(id)>=8 and len(id)<=20 :
                    break
                else:
                    print("your user id must be  of 8-20 characters")
                    id = input("Create your user id : ")
            print("-" * 50)
            print("(1)Your password should be between 6-20 characters\n(2)Use a combination letters, numbers and sysmbols for better secuirity")
            pas=input("Create a strong password : ")
            while n > 0:
                if len(pas)>=6 and len(pas)<=20 :
                    break
                else:
                    print("Your user password must be  of 8 characters")
                    pas = input("Create your user password : ")
            print("-" * 50)
            phn=input("Please enter your phone number : ")
            while n > 0:
                if len(phn)==10:
                    break
                else:
                    phn = input("Please enter a valid phone number : ")
            print("We will be sending you an OTP to your provided phone number")
            ver=input(f"Please enter the OTP send to your phone number ending with {phn[7:]} : ")
            otp()
            while ver != otp_n:
                ver=input("Please enter a valid OTP : ")
            print("-" * 50)
            eml=input("Please enter your email address : ")
            print("-" * 50)
            ver = input("Please enter the OTP send to your email address : ")
            while ver != otp_n:
                ver=input("Please enter a valid OTP : ")
            print("-" * 50)
            am=input("Please enter your amount to be saved : ")
            print("-" * 50)
            acc_no=account()
            data[acc_no]=[{"name":nam,
                       "user_id":id,
                       "password":pas,
                       "phone":phn,
                       "email":eml,
                       "amount":am}]
            write_json(data)
            cust=data[acc_no]
            name=cust[0]['name']
            usr=cust[0]['user_id']
            address=cust[0]['email']
            pas=cust[0]['password']
            phn=cust[0]['phone']
            amt=cust[0]['amount']
            new(address,acc_no,name,usr,pas,phn,amt)
            #new_sms(address,acc_no,name,usr,pas,phn,amt)
            print("Your account have been created successfully")
            print("Thank you for choosing us")
            print("Your account number is ",acc_no)
            print("Please don't forget your account number, user id, and password")
            print("Enter 0 to continue ; enter 1 to end")
            u = input("Enter your choise : ")
            if u == '1':
                print("--------------------Thank you---------------------")
                break
            else:
                print("Wrong choise !")
        else:
            print("Wrong choise !")
    ob.quit()
bank()
