import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import os

def send_email(sender,receiver,subject,message,attachement):
    msg = MIMEMultipart()
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=subject
    msg.attach(MIMEText(message))
    filename=attachement
    p=filename
    path=p
    # path=os.path.join(os.getcwd(),filename)
    with open(path,'rb') as f:
        attachement=MIMEApplication(f.read(),_subtype='pdf')
        attachement.add_header('content-Disposition','attachement',filename=filename)
        msg.attach(attachement)
    smtp_server='smtp.gmail.com'
    smtp_port=587
    smtp_username=sender
    smtp_password="wegjxuedgcurcpsa"
    with smtplib.SMTP(smtp_server,smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender,receiver,msg.as_string())
    return ("mail send done")
     


#details of user    
pass1="wegjxuedgcurcpsa"
sender = "005ajeet@gmail.com"
password = pass1
receiver = "21f1000907@ds.study.iitm.ac.in"


