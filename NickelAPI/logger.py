import NickelBot.logger as log
class logger:
    def __init__(self,data):
        self.data = data
        self.pname = data[0]
    def info(self,t):
        log.info(""+self.pname+" ~ "+t)
    def note(self,t):
        log.note(""+self.pname+" ~ "+t)
    def ok(self,t):
        log.ok(""+self.pname+" ~ "+t)
    def warn(self,t):
        log.warn(""+self.pname+" ~ "+t)
    def error(self,t):
        log.error(""+self.pname+" ~ "+t)
