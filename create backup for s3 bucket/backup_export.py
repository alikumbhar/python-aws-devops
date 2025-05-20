
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     backup_folder = os.path.join(destination, f"backup_{timestamp}")
#     print(backup_folder)

import os
import shutil
import datetime

def back_up(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source) #this is used to compress files


source = r"C:\Users\PMLS\Desktop\python" #source path that folder you want to create backup
destination = r"C:\Users\PMLS\Desktop\python\ebackups" # destination folder where your created backup will be stored

back_up(source, destination)