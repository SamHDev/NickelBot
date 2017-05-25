cmds = []
class CmdListner:
    def __init__(self,name,func):
        self.name = name
        self.func = func
        self.desc = ""
        self.useg = name + ""
        cmds.append(self)
    def InvokeCmd(bot,name,assets,args):
        self.func(bot,assets,args)
    def EditAddt(at,vl):
        if (at == "desc"):
            self.desc = vl
        if (at == "useg"):
            self.useg  = vl
