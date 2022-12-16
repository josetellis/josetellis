import threading
class Demo(threading.Thread):
    def __init__(self):super().__init__()
obj=Demo()
obj.start()