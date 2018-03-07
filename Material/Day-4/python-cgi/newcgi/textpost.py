#! c:\python27\python.exe
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<form action="/cgi-bin/textbox.py" method="post" target="_blank"> '
print '<textarea name="textcontent" cols="40" rows="4">'
print 'Type your text here...'
print '</textarea>'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</html>'