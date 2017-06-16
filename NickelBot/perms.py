import NickelBot as main
import NickelBot as api
from NickelAPI import assets as ass
import json

    

def getFile():
    cfgf = main.config.GetConfigFile("servers")
    with open(cfgf) as data_file:    
        data = json.load(data_file)
    return data
def WriteFile(jsonf):
    cfgf = main.config.GetConfigFile("servers")
    with open(cfgf, 'w+') as outfile:
        json.dump(jsonf,outfile)
def cP(serverid):
    file = getFile()
    file[serverid] = [{}]
    file[serverid][0]["perms"] = [{}]
    file[serverid][0]["perms"][0]["users"] = [{}]
    file[serverid][0]["perms"][0]["users"][0]["4"] = []
    file[serverid][0]["perms"][0]["users"][0]["3"] = []
    file[serverid][0]["perms"][0]["users"][0]["2"] = []
    file[serverid][0]["perms"][0]["users"][0]["1"] = []
    file[serverid][0]["perms"][0]["roles"] = [{}]
    file[serverid][0]["perms"][0]["roles"][0]["4"] = []
    file[serverid][0]["perms"][0]["roles"][0]["3"] = []
    file[serverid][0]["perms"][0]["roles"][0]["2"] = []
    file[serverid][0]["perms"][0]["roles"][0]["1"] = []
    file[serverid][0]["blacklist"] = []
    file[serverid][0]["settings"] = [{}]
    WriteFile(file)
def GetPerms(user,server):
    uid = user.getId()
    level = None
    flu = getFile()[server.getId()][0]["perms"][0]["users"][0]
    flr = getFile()[server.getId()][0]["perms"][0]["roles"][0]
    if uid in flu[4]:
        level = 4
        return level
    elif uid in flu[3]:
        level = 3
        return level
    elif uid in flu[2]:
        level = 2
        return level
    elif uid in flu[1]:
        level = 1
        return level
    if level == None:
        for r in flr[4]:
            if rlr in user.getRolesIds():
                level = 4
                return level
        for r in flr[3]:
            if rlr in user.getRolesIds():
                level = 3
                return level
        for r in flr[2]:
            if rlr in user.getRolesIds():
                level = 2
                return level
        for r in flr[1]:
            if rlr in user.getRolesIds():
                level = 1
                return level
    if level == None:
        return 0
        
def LinkRole(serverid,roleid,level):
    file = getFile()
    file[serverid][0]["perms"][0]["roles"][0][level].append(roleid)
    WriteFile(file)

def UnLinkRole(serverid,roleid):
    file = getFile()
    er = []
    for level in range(1,5):
        try:
            file[serverid][0]["perms"][0]["roles"][0][str(level)].remove(roleid)
            er.append(True)
        except:
            er.append(False)
    WriteFile(file)
    if True in er:
        return True
    else:
        return False

def LinkUser(serverid,userid,level):
    file = getFile()
    file[serverid][0]["perms"][0]["users"][0][level].append(userid)
    WriteFile(file)


def UnLinkUser(serverid,userid):
    file = getFile()
    er = []
    for level in range(1,5):
        try:
            file[serverid][0]["perms"][0]["users"][0][str(level)].remove(userid)

            er.append(True)
        except:
            er.append(False)
    WriteFile(file)
    if True in er:
        return True
    else:
        return False


    
def permcmd(m):
    args = []
    args = m.content.lower().split(" ")
    if (len(args) > 1):
        if (args[1] == "addrole"):
            if (len(args) > 3):
                rlid = args[2].replace("<&","")
                rlid = rlid.replace(">","")
                LinkRole(m.server.id,rlid,args[3])
                ass.runAwait(main.bot.client.send_message,m.channel,"Sucessfully linked the Role")
    if (len(args) > 1):
        if (args[1] == "delrole"):
            if (len(args) > 2):
                rlid = args[2].replace("<&","")
                rlid = rlid.replace(">","")
                r = UnLinkRole(m.server.id,rlid)
                if r:
                    ass.runAwait(main.bot.client.send_message,m.channel,"Sucessfully Unlinked the Role")
                else:
                    ass.runAwait(main.bot.client.send_message,m.channel,"**Sorry**, I could not Unlink the Role")
    if (len(args) > 1):
        if (args[1] == "adduser"):
            if (len(args) > 3):
                rlid = args[2].replace("<@","")
                rlid = rlid.replace(">","")
                LinkUser(m.server.id,rlid,args[3])
                ass.runAwait(main.bot.client.send_message,m.channel,"Sucessfully added user.")
    if (len(args) > 1):
        if (args[1] == "deluser"):
            if (len(args) > 2):
                rlid = args[2].replace("<@","")
                rlid = rlid.replace(">","")
                r = UnLinkUser(m.server.id,rlid)
                if r:
                    ass.runAwait(main.bot.client.send_message,m.channel,"Sucessfully Removed the User")
                else:
                    ass.runAwait(main.bot.client.send_message,m.channel,"**Sorry**, I could not Remove the User")
        
   
#cP("global")
#cP("203220835933224960")
