import string
import platform
import os
import json
from NickelBot import logger as log
def GetFileStruct():
    sys = platform.system()
    #sys = "Lunix"
    rt = "\\"
    win = "Windows"
    lnx = "Lunix"
    nil = None
    if (sys == win):
        rt = "\\"
    if (sys == lnx):
        rt = "/"
    if (sys == nil):
        rt = "\\"
    return rt

def GetBaseDir():
    cr = __file__
    sep = GetFileStruct()
    sp = cr.split(sep)
    bk = 1
    con = ""
    #print(sp)
    for fsp in range(0,(len(sp) - (bk + 1))):
        con = con + sp[fsp] + sep
        #print(con)
    #print(con)
    return con

def GetConfigDir():
    configloc = "config"
    bd = GetBaseDir()
    sep = GetFileStruct()
    if (os.path.exists(bd + configloc + sep)):
        return bd + configloc + sep
    else:
        os.mkdir(bd + configloc + sep)
        return bd + configloc + sep

def GetConfigFile(name):
    fx = ".json"
    cd = GetConfigDir()
    con = cd + name + fx + ""
    if (os.path.exists(con)):
        con1 = ""
    else:
        f = open(con,"w+")
        f.write("{}")
        f.close()
    return con

def GetDataDir():
    dataloc = "data"
    bd = GetBaseDir()
    sep = GetFileStruct()
    if (os.path.exists(bd + dataloc + sep)):
        return bd + dataloc + sep
    else:
        os.mkdir(bd + dataloc + sep)
        return bd + dataloc + sep

def GetDataFile(name):
    fx = ".json"
    dd = GetDataDir()
    con = dd + name + fx + ""
    if (os.path.exists(con)):
        con1 = ""
    else:
        f = open(con,"w+")
        f.write("{}")
        f.close()
    return con

def GetDir(nm):
    dataloc = nm
    bd = GetBaseDir()
    sep = GetFileStruct()
    if (os.path.exists(bd + dataloc + sep)):
        return bd + dataloc + sep
    else:
        os.mkdir(bd + dataloc + sep)
        return bd + dataloc + sep
