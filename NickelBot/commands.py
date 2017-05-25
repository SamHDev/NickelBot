import NickelBot.bot as main
cmds = {}


def help():
    helpc = "```"
    commands = []
    for pl in cmds.keys():
        c = cmd[pl]
        co = c.name
        co + co + " - " + c.desc
        co + co + " - " + c.use
        co + co + "\n"
        helpc = helpc + co
    helpc = "```"
    return helpc
    
def InvokeCmd(cmd,cmddata):
    for li in cmd.list:
        li(cmddata)
        
@main.client.event
async def on_message(m):
    
    