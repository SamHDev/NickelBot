from NickelBot.Assets import discordpy as discord
from NickelBot.bot as main
from NickelBot import logger as log
client = main.client
class User:
  def __init__(self,discorduser):
    self.discord = discorduser
    self.name = discorduser.name
    self.id = discorduser.id
    self.mention = discorduser.metion
    self.
  def dm(self,txt):
    client.send_message(self.discord,txt)
    log.info("SendingMessage",db=True)
  def Mention():
    return self.mention
  
class Message:
  def __init__(self,discord):
    self.discord
    self.server = 
    self.author = User
    self.channel = 

class
    