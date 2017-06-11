import NickelAPI as bot

plugin = bot.plugin("Example-Plugin",version="1.0",creator="SamHDev")
plugin.getlogger().info("Hello")
print(plugin.getconfig().read("Main.Hello"))
print(plugin.getconfig().read("Main",dft="HI"))
def memes(Msg,Text,Sender,Location,Args):
    Msg.reply("Hello MemeStar")
plugin.getcmd("memes").addListner(memes)
plugin.getcmd("memes").setDesc("A Simple Test Message")
def DmMe(Msg,Text,Sender,Location,Args):
    Sender.dm("Works?")
plugin.getcmd("dmme").addListner(DmMe)
plugin.getcmd("dmme").setDesc("Check if Bot Dm's are working!")
