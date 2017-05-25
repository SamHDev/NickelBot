elist ["OnEnable","OnUserJoin","OnUserLeave","OnUserKicked","OnUserBanned","OnMessage","OnMessageEdit","OnMessageDelete"]
ev {}
for el in elist:
    ev[el] = []
def InvokeEvent(name,args):
    if name in elist:
        for els in ev[name]:
            els(args)

def RegisterEvent(name,func):
    if name in elist:
        ev[name].append(func)
        
