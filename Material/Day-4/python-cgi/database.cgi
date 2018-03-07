#!c:\python27\python.exe

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
a=first_name
b=last_name
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (a,b)
print "</body>"
print "</html>"

#database
import MySQLdb
x=MySQLdb.connect('localhost','root','','test')
y=x.cursor()
s='insert into test1 values ("%s","%s")' % (a,b)
y.execute(s)
x.commit()
x.close()

