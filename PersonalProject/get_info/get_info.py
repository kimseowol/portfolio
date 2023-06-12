import csv
import os
import glob
import re

csv_path = os.path.expanduser("~/test/csv_data.csv")


def image_info():
    mylist=[]
    for roots,dirs,files in os.walk("/home/rapa/project"):
        for dir in dirs:
            file_paths = os.path.join(roots,dir)

            file_list = glob.glob(file_paths+"/*.jpg")
            frame = len(file_list)

            info = {"project name":None,"seq name":None,'shot name':None,'version':None,'frame':None,'path':None}
            m_path = re.search('/home/rapa/project/(\w+)/shot/(\w+)/(\w+)/(\w+)/(\w+)',file_paths)
            #print(m_path)

            if m_path:
                #print(m_path)
                info["project name"] = m_path.group(1)
                info["seq name"] = m_path.group(2)
                info["shot name"] = m_path.group(3)
                info["version"] = m_path.group(5)
                info["frame"] = frame
                info["path"] = file_paths
                mylist.append(info)
            #print(mylist)
    return mylist


with open(csv_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["project name","seq name",'shot name','version','frame','path'])
    for i in range(len(image_info())):
        writer.writerow([image_info()[i]['project name'],image_info()[i]['seq name'],image_info()[i]['shot name'],image_info()[i]['version'],image_info()[i]['frame'],image_info()[i]['path']])