import smtplib
from email.mime.text import MIMEText

body = 'This is a test email.'

msg = MIMEText(body)

msg['From'] = ''  # replace with your own
msg['To'] = ''  # replace with your own
msg['Subject'] = 'Hello'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('username', 'password')  # replace with your own

server.send_message(msg)

print('Mail sent.')

server.quit()
