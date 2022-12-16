import os
import threading 
from SearchFileDB import SerachDB
import  logging
from SearchLogging import  searchLog
from FilenotFound import Error
class FileSearcher(threading.Thread):
    drive=""
    file_name=""
    def __init__(self):
        pass

    def search_for_file(self, drive, file_name):

        try:
            print('This is a file searcher.')
            file_paths = []
            drv=drive+":\\"
            print(drv)
            for root, dirs, files in os.walk(drv):
                for name in files:
                    if name == file_name:
                        path = os.path.abspath(os.path.join(root, name))
                        file_paths.append(path)
                        self.search_for_file(self, drive, file_name)
        except:
            print("There was an error")
                    
        return file_paths

    def run(self):
        self.search_for_file(self.drive, self.file_name)
if __name__=='__main__':
    data=[]
    drive=input("Enter the Drive")
    filename=input("Enter the file name")

    obj=FileSearcher()
    dbobj=SerachDB()
    searchLg=searchLog()
    logging.exception()
    res=dbobj.searchDB(filename)
    if res==0:

        data=obj.search_for_file(drive,filename)
        if data:
            raise Error("File Not Found")
        print(data)
        dbobj.insertDB(data[0])
        logging.info(data[0])
    else:
        print(res)






