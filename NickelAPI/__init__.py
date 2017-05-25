import NickelAPI.logger as apilog
import NickelBot.logger as log
import NickelAPI.config as apicfg
import NickelBot.plugin as plld
class plugin:
    def __init__(self,name,creator="Unknown",version="1.0"):
        self.name = name
        self.creator = creator
        self.version = version
        self.file = __file__
        datac = [self.file,self.name,self.version,self.creator,["MEMES"]]
        data = {"name":name,"auth":creator,"ver":version}
        plld.RegisterPlugin(data)
    def getlogger(self):
        data = [self.name,"Test"]
        return apilog.logger(data)
    def getconfig(self):
        data = [self.name,"Test"]
        return apicfg.config(data)
    def getcommand(name):
        
        
        
        
   
