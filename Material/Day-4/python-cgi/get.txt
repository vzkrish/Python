#! c:\python27\python.exe
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<form action="/cgi-bin/hello_get.py" method="get">'
print 'First Name: <input type="text" name="first_name"><br />'
print 'Last Name: <input type="text" name="last_name" />'

print '<input type="submit" value="Submit" />'
print '</form>'
print '</html>'
