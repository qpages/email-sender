import smtplib, json
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "gloutmon@gmx.fr"
    msg['from'] = user
    f = open('password.txt') 
    password = f.read() # see myaccount.google.com to get app password (need 2FA to set up)

    server = smtplib.SMTP("mail.gmx.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()
    f.close()

if __name__ == '__main__':
    email_alert("Hey", "Hello World", "receiver@gmail.com")
