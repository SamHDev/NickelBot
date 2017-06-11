import NickelAPI as bot

import platform
import os
import multiprocessing

plugin = bot.plugin("Host-Info",version="1.0",creator="SamHDev")
plugin.getlogger().info("Host-Info")
#cmd = plugin.getconfig().read("cmd.name",dft="hostinfo")
#print(cmd)
cmd = "host"



def core(Msg,Text,Sender,Location,Args):
    msg = []
    msg.append("**Specs**")
    msg.append("```")
    msg.append("OS: " + platform.uname()[0] + platform.uname()[2])
    msg.append("CPUS: " + str(multiprocessing.cpu_count()))

    msg.append("```")
    ll = " \n ".join(msg)
    Msg.reply(ll)
              
plugin.getcmd(cmd).addListner(core)
plugin.getcmd(cmd).setDesc("Get The Spec's of the HostServer")
