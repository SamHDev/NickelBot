import NickelBot.Assets.discordpy as ds
import NickelBot as main
from NickelAPI import assets as api
from NickelBot import commands as cmdb
from NickelBot import perms as pms
import json
import asyncio
invoke = "!"
token = ""
cfgf = main.config.GetConfigFile("config")
f = open(cfgf,"r+")
cfg = json.load(f)
f.close()
token = cfg["discord"][0]["token"]

shdyn = cfg["discord"][0]["shardmode"]
shdid = cfg["discord"][0]["shardid"]
shdct = cfg["discord"][0]["shardcount"]

invoke = cfg["cmds"][0]["invoke"]

if shdyn == False:
    client = ds.Client()
    main.logger.note("Client Created - NormalMode")
else:
    client = ds.Client(shard_id=shdid,shard_count=shdct)
    main.logger.note("Client Created - ShardMode ["+str(shdid)+"/"+str(shdct)+"]")


api.client = client

@client.event
async def on_ready():
    main.logger.ok("Bot Connected")

@client.event
async def on_message(m):
    if (m.author.id == client.user.id):
        return
    if (m.content.startswith(invoke)) == False:
        return
    if (m.content.startswith(invoke + "help")):
        await client.send_message(m.channel,main.commands.CoreCmd.help())
        return
    if (m.content.startswith(invoke + "pl")):
        await client.send_message(m.channel,main.commands.CoreCmd.plugin())
        return
    if (m.content.startswith(invoke + "perms")):
        pms.permcmd(m)
        return
    ls = api.Message(m)
    mm = ls.getself()
    cmd = ls.getArgs()
    main.commands.InvokeCmd(cmd,mm)

    
def StartConnect():
    main.logger.note("Connecting to Discord")
    try:
        client.run(token)
    except:
        main.logger.fatal("10","Failed to Connect to Discord")
