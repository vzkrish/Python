
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

me = 'prasad.yamijala@gmail.com'
password = 'yamijala'
server = 'smtp.gmail.com:587'
you = 'prasad.yvs@hotmail.com'

text = """
Hello, Friend.

Here is your data:

{table}

Regards,

Me"""

html = """
<html><body><p>Hello, Friend.</p>
<p>Here is your data:</p>
{table}
<p>Regards,</p>
<p>Me</p>
</body></html>
"""
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""


message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])

message['Subject'] = "contents in message body of the mail"
message['From'] = me
message['To'] = you
server = smtplib.SMTP(server)
server.ehlo()
server.starttls()
server.login(me, password)
server.sendmail(me, you, message.as_string())
server.quit()
