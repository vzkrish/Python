import ftplib,sys
x=ftplib.FTP('ftp.sunet.se','anonymous', 'anonymous@sunet.se')
print 'connection established'

# display the directory of the remote machine
data=[]
x.dir(data.append)
print 'directory listing of the remote machine'
for m in data:
    print m
print 

# retrieve a textfile from the remote machine to the localmachine
# display on the screen
print 'displaying robots.txt on the localmachine screen'
x.retrlines('RETR '+ 'robots.txt',sys.stdout.write)
print 

#retrieve to a local file
fo=open('myfile.txt','w')
x.retrlines('RETR '+'robots.txt',fo.write)
fo.close()
print 'file downloaded'
print

# retrieve a binary file
fo1=open('local.html','wb')
x.retrbinary('RETR '+ 'HEADER.html',fo1.write)
fo1.close()
print 'file downloaded'
print


# store file into the remote machine
x.storlines('STOR ' + 'myfile.txt', open('myfile.txt','r'))
x.storbinary('STOR ' + 'local.html',open('local.html','rb'))

#connection closing
print 'closing the connection'
x.close()
             
