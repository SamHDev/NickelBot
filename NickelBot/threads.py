import threading
class FuncThread (threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func = func
    def run(self):
        func = self.func
        func()
