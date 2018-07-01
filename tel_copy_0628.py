from ftplib import FTP
import os
ftp = FTP()
ftp.connect('127.0.0.1')
ftp.login(user='', passwd='')
# print(ftp.getwelcome())
# ftp.dir()
date = '20150629'
# tel_num = '8663187' #电话号
# filename = '151449-O-0006-8663184-S.wav' #文件名

bufsize = 1024
# ftp.cwd(date+'/'+tel_num)  #切换目录
# ftp.dir()
a = []
a.append(ftp.retrlines('nlst'))

# print(ftp.pwd())


def down_rec():
    file_handle = open(filename, "wb").write
    bufsize = 1024
    ftp.retrbinary("RETR " + filename, file_handle, bufsize)
    print('已下载文件', filename)


# down_rec() #下载
