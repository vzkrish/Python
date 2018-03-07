#! c:\python27\python.exe
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<form action="/cgi-bin/dropdown.py" method="post" target="_blank">'
print '<select name="dropdown">'
print '<option value="Maths" selected>Maths</option>'
print '<option value="Physics">Physics</option>'
print '</select>'
print '<input type="submit" value="Submit"/>'
print '</form>'
print '</html>'