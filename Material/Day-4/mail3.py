
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

me = 'prasad.yamijala@gmail.com'
password = 'yamijala'
server = 'smtp.gmail.com:587'
you = 'prasad.yvs@hotmail.com'


text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <table style="width:100%">
  <tr>
    <th>Firstname</th>
     <th>Lastname</th> 
    <th>Age</th>
   </tr>
  <tr>
    <td>Jill</td>
     <td>Smith</td> 
    <td>50</td>
   </tr>
  <tr>
    <td>Eve</td>
     <td>Jackson</td> 
    <td>94</td>
   </tr>
</table> 
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
