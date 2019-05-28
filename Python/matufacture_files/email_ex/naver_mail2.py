import smtplib
#from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

email_list = ['shuttlecock@naver.com, ssintico0801@gmail.com']

password = getpass('Password :')
msg = MIMEMultipart()
msg['Subject'] = '권고사직서'
msg['from'] = 'ssintico88@naver.com'
msg['To'] = ','.join(email_list)
html = """
<html>
    <body>
    <img src = "https://www.catster.com/wp-content/uploads/2018/07/Savannah-cat-long-body-shot.jpg">
    <p> HI </p>
    <a href = "https://www.naver.com"> GO TO NAVER </a>
    </body>
</html>
"""

part = MIMEText(html, 'html')
msg.attach(part)

s = smtplib.SMTP_SSL('smtp.naver.com', 465)
s.login('ssintico88', password)
s.send_message(msg)

print('메일 전송 완료')