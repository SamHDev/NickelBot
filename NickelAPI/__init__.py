import NickelAPI.logger as apilog
import NickelBot.logger as log
import NickelAPI.config as apicfg
import NickelBot.plugin as plld
import NickelAPI.cmd as apicmd
import NickelAPI.events as apiev
from NickelBot import commands as bcmd
class plugin:
    def __init__(self,name,creator="Unknown",version="1.0"):
        self.name = name
        self.creator = creator
        self.version = version
        self.file = __file__
        datac = [self.file,self.name,self.version,self.creator,["MEMES"]]
        data = {"name":name,"auth":creator,"ver":version}
        plld.RegisterPlugin(self.file,self.name,self.version,self.creator)
    def getlogger(self):
        data = [self.name,"Test"]
        return apilog.logger(data)
    def getconfig(self):
        data = [self.name,"Test"]
        return apicfg.config(data)
    def getcmd(self,name):
        return apicmd.GetCommand(name,self)
    def addEvent(self,name,func):
        r = ev.RegisterEvent(name,func)
        return
        
        
        
        
        
        
        
   
