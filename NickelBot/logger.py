#from termcolor import colored
import sys
dbug = False
def SetDebug(v):
  dbug = bool(v)
def WriteConsoleLog(col,tpe,txt):
    pre = "LOG"
    sep = " >>> "
    end = '\033[0m'
    col = ""
    end = ""
    if (col == None):
        print("[" +pre+ "] " + tpe + sep + txt)
    else:
        print(col + " [" +pre+ "] " +  tpe + sep + txt + end)
def info(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"DEBUG - INFO",t)
  elif db == False:
    WriteConsoleLog(None,"INFO",t)
def note(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"DEBUG - NOTE",t)
  elif db == False:
    WriteConsoleLog(None,"NOTE",t)
def ok(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"DEBUG - -OK-",t)
  elif db == False:
    WriteConsoleLog(None,"-OK-",t)
def warn(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"DEBUG - WARN",t)
  elif db == False:
    WriteConsoleLog(None,"WARN",t)
def error(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"DEBUG - ERRR",t)
  elif db == False:
    WriteConsoleLog(None,"ERRR",t)
def fatal(eid,msg):
    ei = 000
    if (len(eid) == "1"):
        ei = "00" + eid
    if (len(eid) == "2"):
        ei = "0" + eid
    if (len(eid) == "3"):
        ei = "" + eid
    WriteConsoleLog(None,"FATL","An Error Occured" + "ERROR: " + str(ei))
    WriteConsoleLog(None,"ERRR","" + msg)
    import NickelBot
    NickelBot.CloseBot()
    sys.exit(0)
