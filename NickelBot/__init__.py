def StartBot():
    from NickelBot import config as cfg
    from NickelBot import logger as log
    log.ok("Bot Starting")
    from NickelBot import plugin as plg
    plg.GetPlugins()
    from NickelBot import console as cns
    cns.StartConsole()
