import smtplib
from email.message import EmailMessage
from getpass import getpass

email_list = ['shuttlecock@naver.com, ssintico0801@gmail.com']

password = getpass('Password :')
msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['from'] = 'ssintico88@naver.com'
msg['To'] = ','.join(email_list)
msg.set_content('님 ㅂㅇ')

s = smtplib.SMTP_SSL('smtp.naver.com', 465)
s.login('ssintico88', password)
s.send_message(msg)

print('메일 전송 완료')