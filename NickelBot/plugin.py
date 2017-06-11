#lcl
from NickelBot import config as cfg
from NickelBot import logger as log
#ext
import importlib.util
import imp
from os import listdir
from os.path import isfile, join
import os
plugins = []
def GetPlugins():
    log.info("Getting Plugins")
    pl = cfg.GetDir("plugins")
    files = [f for f in listdir(pl) if isfile(join(pl, f))]
    log.note("Found " + str(len(files)) + " Plugins")
    log.info("Loading Plugins")
    flc = 0
    for fl in files:
        #try:
        if True:
            full_path_to_module = pl + "" + fl
            module_dir, module_file = os.path.split(full_path_to_module)
            module_name, module_ext = os.path.splitext(module_file)
            log.info("Loading Plugin: " + str(module_name))
            #print(str(full_path_to_module) + "|" + str(module_dir) + "|" +  str(module_file) + "|" +  str(module_name) + "|" +  str(module_ext))
            #save_cwd = os.getcwd()
            #os.chdir(module_dir)
            mfile, mpathname, mdescription = imp.find_module(module_name, [module_dir])
            imp.load_module(module_name, mfile, mpathname, mdescription)
            #os.chdir(save_cwd)
            flc = flc + 1
            log.info("Loaded Plugin: " + str(module_name))
        #except:
        if False:
            log.error("ERROR While Loading Plugin: " + str(module_name))
        log.note("Loaded " + str(flc) + " Plugins")
        log.info("Plugins Loaded")

def RegisterPlugin(file,name,v,auth):
    bp = BotPlugin(name,file,v,auth,[])
    plugins.append(bp)
    log.note("Plugin: " + name + " V:" + v + " by " + auth)
class BotPlugin:
    def __init__(self,name,file,version,creator,data):
        self.name = name
        self.file = file
        self.version = version
        self.author = creator
        self.desc = ""
        self.data = data
    def GetInfo():
        data = [self.name,self.file,self.version,self.author]
        return data
