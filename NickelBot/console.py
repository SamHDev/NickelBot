from NickelBot import logger as log
from NickelBot import threads as thd
import time
ls = {}
def ConsoleCommand(name,func):
    ls[name] = func
#commands
def TestCmd(args):
    log.note("Test")
    log.warn("Test")
    log.error("Test")
    log.info("Test")
    log.ok("Test")
def exit(args):
  try:
    time.sleep(args[1])
    input("-PRESS ENTER TO EXIT--")
  except:
    input("-PRESS ENTER TO EXIT--")
  os.exit(1)
    
#end of commands
def Console():
    x = "0"
    ConsoleCommand("test",TestCmd)
    while x == "0":
        try:
            cmd = input(" [Console]  >>> ")
            pl = cmd.lower().split(" ")
            ls[pl[0]](pl)
        except:
            log.warn("Command Does not Exist")

def StartConsole():
    mt = thd.FuncThread(Console)
    mt.run()
