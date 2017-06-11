from NickelBot import bot as main
from NickelBot import logger as log
from NickelBot import plugin as pl
cmds = {}

class CoreCmd:
    def help():
        helpc = "```"
        helpc = helpc + "Name  -  Description  -  Usage \n"
        commands = []
        for pl in cmds.keys():
            c = cmds[pl]
            co = c.name
            co = co + " - " + c.desc
            co = co + " - " + c.use
            co = co + "\n"
            helpc = helpc + co
        helpc = helpc + "```"
        return helpc
    def plugin():
        plgs = pl.plugins
        plc = "```"
        plc = plc + "Name - Version - Author \n"
        for plg in plgs:
            plc = plc + plg.name + "  -  " + plg.version + "  -  " + plg.author + "\n"
        plc = plc + "```"
        return plc
    def dm():
        print("Hello")
        
   
def InvokeCmd(cmd,cmddata):
    #try:
    if True:
        cmdd = cmds[cmd[0]]
        for li in cmdd.getLists():
            li(cmddata,cmddata.text,cmddata.user,cmddata.location,cmddata.args)
    #except:
    #    log.warn("Command: '" + cmddata.args[0] + "' Not Found")
