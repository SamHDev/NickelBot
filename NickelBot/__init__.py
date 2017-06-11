import NickelBot.config as cfg
import NickelBot.logger as log
import NickelBot.threads as thd
import NickelBot.bot as bot
import NickelBot.plugin as plg
import NickelBot.console as cns
k = thd.FuncThread(bot.StartConnect)
def StartBot():
    log.ok("Bot Starting")
    plg.GetPlugins()
    k.start()
    #l = thd.FuncThread(cns.StartConsole)
    #l.start()
    try:
        while True:
            h = ""
    except KeyboardInterrupt:
        CloseBot()
    except SystemExit:
        CloseBot()

def CloseBot():
    bot.client.logout()
    k.stop()
    #l.stop()
    print("Closed :)")
