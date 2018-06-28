from ftplib import FTP 

ftp = FTP()
ftp.connect('127.0.0.1')
ftp.login(user='',passwd='')
print(ftp.getwelcome())