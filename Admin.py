import json
import requests
import random
import sys
import smtplib as s
obs = s.SMTP("smtp.gmail.com", 587)
obs.starttls()
obs.login("uddalakmukhopadhyay@gmail.com","Uddalak2005")
with open("user_det.json") as json_file:
    data=json.load(json_file)
def otp():
    global otp_n
    otp_n=str(random.randint(1000,9999))
##############################################################################
def account():
    num=random.randint(100000,999999)
    n=1
    while n>0:
        if num not in data:
            return num
            break
###########################################################################
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
##############################################################################
def email(address,ot):
    global obs
    subject = "Horizon Bank of India"
    body = "Your one time pass word for transaction is " + ot + ".\nDon't Share it with anyone"
    messege = "Subject:{}\n\n{}".format(subject, body)
    obs.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
##############################################################################
def write_json(data,filename="user_det.json"):
    with open(filename, 'w') as f:
        json.dump(data,f,indent=4)
#############################################################################
def confirm_sms(address,acc_no,name,usr,pas,phn,amt):
    text="We are very glad to inform you that your account info have been updated as per as your requests.Your updated credentials are as follows - \n"+"Name - "+str(name)+"\nAccount number - "+str(acc_no)+"\nUser ID - "+str(usr)+"\nPassward - "+str(pas)+"\nPhone numebr - "+str(phn)+"\nEmail ID - "+str(address)+"\nAmount deposited -  INR "+str(amt)+"\n\nThank you for choosing us"
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
########################################################################
def confirm_email(address,acc_no,name,usr,pas,phn,amt):
    subject="Credentials Updated"
    body="We are very glad to inform you that your account info have been updated as per as your requests.Your updated credentials are as follows - \n"+"Name - "+str(name)+"\nAccount number - "+str(acc_no)+"\nUser ID - "+str(usr)+"\nPassward - "+str(pas)+"\nPhone numebr - "+str(phn)+"\nEmail ID - "+str(address)+"\nAmount deposited -  INR "+str(amt)+"\n\nThank you for choosing us"
    messege = "Subject:{}\n\n{}".format(subject, body)
    obs.sendmail("uddalakmukhopadhyay@gamil.com", address, messege)
########################################################################
def admin():
    global data
    n=1
    print("-"*50)
    print("Welcome sir !")
    usr=input("Please enter your user ID is : ")
    print(data[usr])
    while usr !="horizon_bnk" and n != 6:
        if n==5:
            print("You have entered wrong user ID for 5 times.\nPlease try again later")
            sys.exit()
        print("Please enter a valid user ID")
        usr = input("Please enter a valid user ID : ")
        n+=1
    admin=data[usr]
    pas=input("Please enter your passward : ")
    n=1
    while pas != admin[0]['password']:
        if n==5:
            print("You have entered wrong passward for 5 times.\nPlease try again later")
            sys.exit()
        print("Please enter a valid passward")
        usr = input("Please enter a valid passward : ")
        n+=1
    otp()
    em = admin[0]['email']
    phn = admin[0]['phone']
    #sms(phn, otp_n)
    email(em, otp_n)
    ver=input("Please enter the 4-digit OTP send on your phone number\nand in your email : ")
    a=1
    while ver != otp_n:
        print("You have entered wrong OTP")
        ver=input("Plese enter a valid OTP : ")
    while a>0:
        acc=input("Please enter the account number of the customer : ")
        while acc not in data:
            acc=input("Please enter a valid account number : ")
        print("Enter \'1\' to change the account number customer.\nEnter \'2\' to change the user id of the customer.\nEnter \'3\' to chnage the password of the customer.\nEnter \'4\' to change the phone number of the customer.\nEnter \'5\' to change the email address of the customer.")
        ch=input("Enter your choise : ")
        cust=data[acc]
        if ch=="1":
            name = cust[0]['name']
            usr = cust[0]['user_id']
            address = cust[0]['email']
            pas = cust[0]['password']
            phn = cust[0]['phone']
            amt = cust[0]['amount']
            nm=account()
            data[nm]=[
                {
                    "name":name,
                    "user_id":usr,
                    "password":pas,
                    "phone":phn,
                    "email":address,
                    "amount":amt
                }
            ]
            data.pop(acc)
            write_json(data)
        elif ch=="2":
            us=input("Enter the new user ID to be saved : ")
            cust[0]['user_id']=us
            write_json(data)
        elif ch=="3":
            pas=input("Enter the new password to be saved : ")
            cust[0]['password']=pas
            write_json(data)
        elif ch=="4":
            ph=input("Enter the new phone number to be saved : ")
            cust[0]['phone']=ph
            write_json(data)
        elif ch=="5":
            em=input("Enter the new email address to be saved : ")
            cust[0]['email']=em
            write_json(data)
        else:
            print("Wrong choise !")
        name = cust[0]['name']
        usr = cust[0]['user_id']
        address = cust[0]['email']
        pas = cust[0]['password']
        phn = cust[0]['phone']
        amt = cust[0]['amount']
        op=input("Enter \'1\' to exit; or \'2\' to continue : ")
        #confirm_sms(address,acc,name,usr,pas,phn,amt)
        confirm_email(address, acc, name, usr, pas, phn, amt)
        if op=="1":
            break
    obs.quit()
admin()