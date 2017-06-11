from NickelBot import config as cfg
import os
import json
class config:
    def __init__(self,data):
        self.data = data
        ls = self.reload(data[0])
        self.ls = ls
    def reload(self,filename):
        cf = "config.json"
        ldr = cfg.GetDir("plugins")
        sep = cfg.GetFileStruct()
        dr = ldr + filename + sep
        #print(dr)
        #print(dr + cf)
        if (os.path.exists(dr) == False):
            os.mkdir(dr)
        elif (os.path.exists(dr + cf) == False):
            f = open(dr + cf,"w")
            f.write("{}")
            f.close()
        print(dr + cf)
        with open(dr + cf) as json_dump:
            json_load = json.load(json_dump)
        return [json_load,dr + cf]
    def read(self,path,dft="None"):
        data = self.ls
        pl = '["'
        #print(pl)
        pl = pl + path.replace(".",'"][0]["')
        #print(pl)
        pl = pl + '"]'
        #print(pl)
        pl = "data" + pl
        try:
            rd = exec(pl)
        except:
            rd = dft
        return rd
    def write(self,path,txt):
        data = self.ls
        #CreatingSections
        sp = path.split(".")
        if len(sp) > 0 :
            fp = 'data'    
            for spin in range(0,len(sp) - 1):
                fp = fp + "[" + sp[spin] + "]"
                cn = False
                try:
                     if ((exec(fp) == None) == False):
                        cn = True
                except:
                    cn = True
                if (cn):
                    exec(fp + " = []")
                fp = fp + "[0]"
        
        pl = '["'
        #print(pl)
        pl = pl + path.replace(".",'"][0]["')
        #print(pl)
        pl = pl + '"]'
        #print(pl)
        pl = "data" + pl + "=" + txt
        try:
            exec(pl)
        except:
            d = 1

            
class jsonfile:
    def __init__(self,data):
        self.data = data
        self.path = data[1]
        ls = self.reload(data[0])
        self.ls = ls
    def reload(self,filename):
        cf = "config.json"
        ldr = cfg.GetDir("plugins")
        sep = cfg.GetFileStruct()
        dr = ldr + filename + sep
        #print(dr)
        #print(dr + cf)
        if (os.path.exists(dr) == False):
            os.mkdir(dr)
        elif (os.path.exists(dr + cf) == False):
            f = open(dr + cf,"w")
            f.write("{}")
            f.close()
        with open(dr + cf) as json_dump:
            json_load = json.load(json_dump)
        return [json_load,dr + cf]
    def read(self,path,dft="None"):
        data = self.ls
        pl = '["'
        #print(pl)
        pl = pl + path.replace(".",'"][0]["')
        #print(pl)
        pl = pl + '"]'
        #print(pl)
        pl = "data" + pl
        try:
            rd = exec(pl)
        except:
            rd = dft
        return rd
    def write(self,path,txt):
        data = self.ls
        #CreatingSections
        sp = path.split(".")
        if len(sp) > 0 :
            fp = 'data'    
            for spin in range(0,len(sp) - 1):
                fp = fp + "[" + sp[spin] + "]"
                cn = False
                try:
                     if ((exec(fp) == None) == False):
                        cn = True
                except:
                    cn = True
                if (cn):
                    exec(fp + " = []")
                fp = fp + "[0]"
        
        pl = '["'
        #print(pl)
        pl = pl + path.replace(".",'"][0]["')
        #print(pl)
        pl = pl + '"]'
        #print(pl)
        pl = "data" + pl + "=" + txt
        try:
            exec(pl)
        except:
            d = 1
