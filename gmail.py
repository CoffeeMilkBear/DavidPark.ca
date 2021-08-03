from google.cloud import secretmanager
import os
import smtplib

proxyEmail = 'junarvi@gmail.com'
password = None

def getPassword():
  client = secretmanager.SecretManagerServiceClient()
  secretVersion = client.access_secret_version(request={'name': 'projects/map-collector-314202/secrets/gmail-password/versions/latest'})
  password = secretVersion.payload.data.decode('UTF-8')
  return password

def sendProxyEmail(sender, to, body):
  global password
  global proxyEmail
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    if password is None:
        password = getPassword()
    smtp.login(proxyEmail, password)

    defaultSubject = 'A visitor left you a message on davidpark.me'
    footer = '<This message was sent to you by a visitor from davidpark.me>'

    msg = f'Subject: {defaultSubject}\n\nFrom: {sender}\n\n{body}\n\n{footer}'

    smtp.sendmail(proxyEmail, to, msg)
