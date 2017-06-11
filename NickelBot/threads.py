import threading
class FuncThread (threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func = func
    def run(self):
        func = self.func
        func()
    def end(self):
        self._stop_event.set()
    def execute():
        self.start()
    def stopped(self):
        return self._stop_event.is_set()
    def stop(self):
        self.stopped = True
def runThread(Func):
    lll = FuncThread(Func)
    lll.run()
    
