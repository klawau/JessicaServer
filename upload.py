from ftplib import *

ftp = FTP("lidemice.com","u988860555", "y4m4n3mr3") #save a line and just put your U:P here.

def upload_file(file_name,data):
    ftp.cwd("/public_html/forum3")#Directory 
    ftp.storbinary('STOR %s' % file_name, data)
ftp.quit()
