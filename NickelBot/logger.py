#from termcolor import colored
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
    WriteConsoleLog(None,"INFO",t)
  elif db = False:
    WriteConsoleLog(None,"DEBUG - INFO",t)
def note(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"NOTE",t)
  elif db = False:
    WriteConsoleLog(None,"DEBUG - NOTE",t)
def ok(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"-OK-",t)
  elif db = False:
    WriteConsoleLog(None,"DEBUG - -OK-",t)
def warn(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"WARN",t)
  elif db = False:
    WriteConsoleLog(None,"DEBUG - WARN",t)
def error(t,db=False):
  if db and dbug:
    WriteConsoleLog(None,"ERRR",t)
  elif db = False:
    WriteConsoleLog(None,"DEBUG - ERRR",t)
def fatal(eid,msg):
    ei = 000
    if (len(eid) == "1"):
        ei + "00" + eid
    if (len(eid) == "2"):
        ei + "0" + eid
    if (len(eid) == "3"):
        ei + "" + eid
    WriteConsoleLog(None,"FATL","An Error Occured" + "ERROR: " + ei)
    WriteConsoleLog(None,"ERRR","" + msg)
SetDubug(True)