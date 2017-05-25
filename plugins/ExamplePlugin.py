import NickelAPI as bot

plugin = bot.plugin("Example-Plugin",version="1.0",creator="SamHDev")
plugin.getlogger().info("Hello")
print(plugin.getconfig().read("Main.Hello"))
print(plugin.getconfig().read("Main",dft="HI"))
def memes(Sender,Args,
plugin.getcmd("memes").RegisterListner(memes)
