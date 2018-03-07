import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

#Next, log in to the server
server.login("prasad.yamijala@gmail.com", "yamijala")

#Send the mail
msg="""From: From Prasad <prasad.yamijala@gmail.com>
To: To prasad <prasad.yvs@hotmail.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""

server.sendmail("prasad.yamijala@gmail.com", "prasad.yvs@hotmail.com", msg)




