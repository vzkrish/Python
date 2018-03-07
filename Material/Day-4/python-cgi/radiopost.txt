#! c:\python27\python.exe
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">'
print '<input type="radio" name="subject" value="maths" /> Maths'
print '<input type="radio" name="subject" value="physics" /> Physics'
print '<input type="submit" value="Select Subject" />'
print '</form>'
print '</html>'