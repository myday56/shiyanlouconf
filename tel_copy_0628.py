from ftplib import FTP
import os
ftp = FTP()
ftp.connect('127.0.0.1')
ftp.login(user='', passwd='')
# print(ftp.getwelcome())
# ftp.dir()
date = '20150629'
tel_num = '8663187'
filename = '151449-O-0006-8663184-S.wav'

bufsize = 1024
ftp.cwd(date+'/'+tel_num)
# ftp.dir()

print(ftp.pwd())


def down_rec():
    file_handle = open(filename, "wb").write
    bufsize = 1024
    ftp.retrbinary("RETR " + filename, file_handle, bufsize)


down_rec()
