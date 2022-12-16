import logging
import re
class searchLog():
    def __init__(self):
        logging.basicConfig(filename='filelog.txt',level=logging.INFO)
    def searchLog(self,filename):
        file=open("filelog.txt","r")
        str='joseph.txt'
        data=re.compile(str)
        res=data.search(str)
        line=file.readline()
        print(res.group(0))



if __name__=='__main__':
    f=searchLog()
    f.searchLog()