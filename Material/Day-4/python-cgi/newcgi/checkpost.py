#! c:\python27\python.exe
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<form action="/cgi-bin/checkbox.py" method="POST" target="_blank">'
print '<input type="checkbox" name="maths" value="on" /> Maths'
print '<input type="checkbox" name="physics" value="on" /> Physics'
print '<input type="submit" value="Select Subject" />'
print '</form>'
print '</html>'