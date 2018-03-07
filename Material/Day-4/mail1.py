import smtplib
server = smtplib.SMTP('smtp.live.com', 587)
server.ehlo()
server.starttls()

#Next, log in to the server
server.login("prasad.yvs@hotmail.com", "sreeja@123")

#Send the mail
msg="""From: From Prasad <prasad.yvs@hotmail.com>
To: prasad <prasad.yamijala@gmail.com>
Subject: SMTP e-mail test
This is the reply message to previous mail
Hello!! How are You !!!
"""

server.sendmail("prasad.yvs@hotmail.com", "prasad.yamijala@gmail.com", msg)




