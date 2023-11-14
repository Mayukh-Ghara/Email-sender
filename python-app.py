from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'example@gmail.com'  # You have to put your email id 
email_password = '---- ---- ---- ----' # App pasword of your mail

email_receiver = 'example@soebing.com'  # You have to put email id whome you want to send 

subject = "This will be the subject of this mail"
body = """
This will be the body of this mail
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())