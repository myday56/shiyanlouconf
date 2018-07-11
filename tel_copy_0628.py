from ftplib import FTP
import os

# print(ftp.getwelcome())
# ftp.dir()
url = '192.168.96.55'
date = '20150629'
tel_num = '8663187'
# filename = '151449-O-0006-8663184-S.wav'
lujing = 'C:\\Users\\kfb\\Desktop\\py\\code\\tel'



# ftp.cwd(date+'/'+tel_num)


# print(ftp.pwd())
ftp = FTP(url)
# ftp.connect(url)
ftp.login(user='', passwd='')
tel_date_list = []
tel_date_temp = []
tel_date = []
ftp.dir("",tel_date_list.append)
for x in tel_date_list:
    tel_date_temp.append(x[-8:])
    tel_date = tel_date_temp[2:]
    # ftp.cwd(str(tel_date))
    # break
print(tel_date[0])
ftp.cwd(tel_date[0]+'/'+tel_num)
filename_list = []
filename_temp = []
filename = []
ftp.dir("",filename_list.append)
for x in filename_list:
    filename_temp.append(x[55:])
    filename = filename_temp[2:]
# print(a.split())
print(filename[0])
# def down_rec(): #下载
#     file_handle = open(filename, "wb").write
#     bufsize = 1024
#     ftp.retrbinary("RETR " + filename, file_handle, bufsize)


# down_rec()
# ftp_connect()
# create_dic()  #def create_dic() 定义函数
