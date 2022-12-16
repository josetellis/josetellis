class FileDenied(Exception):
    def __init__(self,msg):
        self.msg=msg

age=34
try:
    age<18


except FileDenied as msg:
    print(msg)
