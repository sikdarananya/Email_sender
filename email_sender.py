from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sikdarananya2000@gmail.com'
email_password = '' #create app passowrds from your Google account
#Google Account
#Security
#Turn on 2 step authentication
#App passwords
#Create app password 


email_receiver = 'sikdarpradipkumar@gmail.com'

subject = "Hi! Its Ananya Sikdar"

body = """
I am a Software Engineer currently employeed with Cognizant
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver

em['subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

