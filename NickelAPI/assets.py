from NickelBot.Assets import discordpy as discord
import NickelBot as main
from NickelBot import bot as bots
from NickelBot import logger as log
from NickelBot import perms as pms
import asyncio
loop = asyncio.get_event_loop()

def runAwait(Func,*Arg):
    l = len(Arg)
    y = None
    if (l == 1):
        if (Arg[0] == None):
            y = asyncio.run_coroutine_threadsafe(Func(),loop)
        else:
            y = asyncio.run_coroutine_threadsafe(Func(Arg[0]),loop)
    if (l == 2):
        y = asyncio.run_coroutine_threadsafe(Func(Arg[0],Arg[1]),loop)
    if (l == 3):
        y = asyncio.run_coroutine_threadsafe(Func(Arg[0],Arg[1],Arg[2]),loop)
    if (l == 4):
        y = asyncio.run_coroutine_threadsafe(Func(Arg[0],Arg[1],Arg[2],Arg[3]),loop)
    if (l == 5):
        y = asyncio.run_coroutine_threadsafe(Func(Arg[0],Arg[1],Arg[2],Arg[3],Arg[4]),loop)
    #loop.close()
    log.info("Await Yield: " + str(y),db=True)
    return y

client = discord.Client()
class User:
  def __init__(self,discorduser):
    self.discord = discorduser
    self.name = discorduser.name
    self.id = discorduser.id
    self.mention = discorduser.mention
    self.hello = ""
  def dm(self,txt):
    runAwait(client.send_message,self.discord,txt)
    log.info("SendingMessage",db=True)
  def Mention():
    return self.mention
  def hasPerms(self,level):
    log.info("Blank",db=True)
    pn = pms.getPerms(self,Server(self.discord.server))
    if (level >= pn):
        return True
    else:
        return False
  def getRolesIds(self):
      rlid = []
      for rl in self.discord.roles:
          rlid.append(rl.id)
      return rlid


class Server:
    def __init__(self,discordc):
        self.discord = discordc
        self.name = discordc.name
        self.owner = User(discordc.owner)
        self.id = User(discordc.owner)
        self.textchannels = []
        self.voicechannels = []
        self.members = []
    def getName(self):
        return self.name
    def getIcon(self):
        return self.discord.icon
    def getID(self):
        return self.id
    def getRoles(self):
        comp = []
        for rl in self.discord.roles:
            comp.append(Role(rl))
        return comp
    def getTextChannels(self):
        for sam in discordc.channels:
            if (sam.type == discord.ChannelType.text):
                self.textchannels.append(Channel(sam))
            if (sam.type == discord.ChannelType.voice):
                self.voicechannels.append(VoiceChannel(sam))
        return self.textchannels
    def getVoiceChannels(self):
        for sam in discordc.channels:
            if (sam.type == discord.ChannelType.text):
                self.textchannels.append(Channel(sam))
            if (sam.type == discord.ChannelType.voice):
                self.voicechannels.append(VoiceChannel(sam))
        return self.voicechannels
    def getOwner(self):
        return self.owner
    def getTextChannel(self,id):
        ids = []
        for iz in self.getTextChannels():
            ids[iz.getID()] = iz
        if (id in ids):
            return ids[id]
        else:
            return None
    def getVoiceChannel(self,id):
        ids = []
        for iz in self.getVoiceChannels():
            ids[iz.getID()] = iz
        if (id in ids):
            return ids[id]
        else:
            return None
    def setName(self,newname):
        try:
            runAwait(client.edit_server,self.discord,name=newname)
            log.ok("Server edited (SetName)",db=True)
            return True
        except discord.Forbidden:
            log.warn("Can't edit Server (SetName): Forbidden")
            return False
        except discord.HTTPException:
            log.warn("Can't edit Server (SetName): Failed")
            return False
    def setIcon(self,newicon):
        try:
            runAwait(client.edit_server,self.discord,name=newicon)
            log.ok("Server edited (SetIcon)",db=True)
            return True
        except discord.Forbidden:
            log.warn("Can't edit Server (SetIcon): Forbidden")
            return False
        except discord.HTTPException:
            log.warn("Can't edit Server (SetIcon): Failed")
            return False
        except discord.InvalidArgument:
            log.warn("Can't edit Server (SetIcon): IconType")
            return False
    def giveOwner(self,newownerid):
        try:
            runAwait(client.edit_server,self.discord,name=newicon)
            log.ok("Server edited (SetOwner)",db=True)
            return True
        except discord.Forbidden:
            log.warn("Can't edit Server (SetIcon): Forbidden")
            return False
        except discord.HTTPException:
            log.warn("Can't edit Server (SetIcon): Failed")
            return False
        except discord.InvalidArgument:
            log.warn("Can't edit Server (SetIcon): NotOwner")
            return False
    def getBans(self):
        try:
            bans = runAwait(client.get_bans,self.discord)
        except discord.Forbidden:
            log.warn("Can't Get Server Info (GetBans): Forbidden")
            return None
        except discord.HTTPException:
            log.warn("Can't Get Server Info (GetBans): Failed")
            return None
        comp = []
        for us in bans:
            comp.append(User(us))
        return comp
    def getInvite(self):
        invs = runAwait(client.invites_from,self.discord)
        iv = None
        for iv in invs:
            if (iv.max_age == 0):
                if (iv.temporary == False):
                    return iv.url

class Role:
    def __init__(self,discordc):
        self.discord = discordc
    def getName(self):
        return self.discord.name


class VoiceChannel:
    def __init__(self,discordc):
        self.discord = discordc
        self.name = discordc.name
        self.id = discordc.id
        self.server = discord.server
    def getName(self):
        return self.name
    def getID(self):
        return self.id
    def getServer(self):
     return self.server
    def getUsers(self):
        comp = []
        for us in self.discord.voice_members:
            comp.append(User(us))
        return comp
    def getLimit(self):
        return self.discord.user_limit
    def SetName(self,newname):
        try:
            runAwait(client.edit_channel,self.discord,name=newname)
            log.ok("Channel Edited (SetName)",db=True)
            return True
        except discord.Forbidden:
            log.warn("Can't edit channel (SetName): Forbidden")
            return False
        except discord.HTTPException:
            log.warn("Can't edit channel (SetName): Failed")
            return False
    def SetLimit(self,newlimit):
        if (newlimit == None):
            newlimit = 0
        try:
            runAwait(client.edit_channel,self.discord,user_limit=newlimit)
            log.ok("Channel Edited (SetLimit)",db=True)
            return True
        except discord.Forbidden:
            log.warn("Can't edit channel (SetLimit): Forbidden")
            return False
        except discord.HTTPException:
            log.warn("Can't edit channel (SetLimit): Failed")
            return False



class Channel:
  def __init__(self,discordc):
    self.discord = discordc
    self.server = Server(discordc.server)
    self.name = discordc.name
    self.id = discordc.id
    self.topic = discordc.topic
  def sendMsg(self,txt):
    try:
      runAwait(client.send_messagem,self.discord,txt)
      log.ok("Sent Message",db=True)
    except:
      log.error("Error Sending Message",db=True)
  def getName(self):
      return self.name
  def getID(self):
     return self.id
  def getServer(self):
      return self.server
  def SetName(self,newname):
     try:
         runAwait(client.edit_channel,self.discord,name=newname)
         log.ok("Channel Edited (SetName)",db=True)
         return True
     except discord.Forbidden:
         log.warn("Can't edit channel (SetName): Forbidden")
         return False
     except discord.HTTPException:
         log.warn("Can't edit channel (SetName): Failed")
         return False
def SetTopic(self,newtopic):
     try:
         runAwait(client.edit_channel,self.discord,topic=newtopic)
         log.ok("Channel Edited (SetTopic)",db=True)
         return True
     except discord.Forbidden:
         log.warn("Can't edit channel (SetTopic): Forbidden")
         return False
     except discord.HTTPException:
         log.warn("Can't edit channel (SetTopic): Failed")
         return False

class Message:
  def __init__(self,discordi):
    self.discord = discordi
    self.location = Channel(discordi.channel)
    self.user = User(discordi.author)
    self.id = discordi.id
    self.text = discordi.content
    self.time = ""
    self.args = self.text.split(" ")
    self.args[0] = self.args[0].replace(bots.invoke,"")
  def getatts(self):
    return [self,self.discord,self.text,self.user,self.location,self.args]
  def getself(self):
      return self
  def getArgs(self):
      return self.args
  def reply(self,txt):
      runAwait(client.send_message,self.discord.channel,txt)
