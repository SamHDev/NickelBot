dinvoke = "!"
import NickelBot.commands as bcmdm
class command:
    def __init__(self,name,plugin):
        self.name = str(name)
        self.plugin = plugin
        self.list = []
        self.invoke = dinvoke
        self.desc = "No Discription"
        self.alis = []
        self.use = self.inovke + self.name
    def addListner(self,func):
        self.list.append(func)
    def setInvoke(self,invoke):
        self.invoke = invoke
    def setDesc(self,desc):
        self.desc = str(desc)
    def addAlt(self,altcmd):
        self.alis.append(str(altcmd))
    def addUsage(self,use):
        self.use = self.invoke + self.name + " " + use
        self.push()
    def push(self):
        bcmd.cmds[self.name] = self

def GetCommand(name,plugin):
    for cmd in bcmd.cmds:
        if (cmd.name == str(name)):
                return cmd
    cmd = command(name,plugin)
    cmd.push()
    return cmd

class CmdData:
    def __init__(self,discord,message,author,location,mentions,mid):
        self.discord = discord
        self.msg = message
        self.user = author
        self.loc = location
        self.ment = mentions
        self.id = mid
    def getRaw(self):
        return self.msg
    def getUser(self):
      
