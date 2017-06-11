import asyncio

def runAwait(Func,*Arg):
    l = len(Arg)
    loop = asyncio.get_event_loop()
    y = None
    if (l == 1):
        if (Arg[0] == None):
            y = loop.run_until_complete(Func())
        else:
            y = loop.run_until_complete(Func(Arg[0]))
    if (l == 2):
        y = loop.run_until_complete(Func(Arg[0],Arg[1]))
    if (l == 3):
        y = loop.run_until_complete(Func(Arg[0],Arg[1],Arg[2]))
    if (l == 4):
        y = loop.run_until_complete(Func(Arg[0],Arg[1],Arg[2],Arg[3]))
    if (l == 5):
        y = loop.run_until_complete(Func(Arg[0],Arg[1],Arg[2],Arg[3],Arg[4]))
    loop.close()
    print(y)
    return y

async def Hello(h):
    print("Hello")
    return "Penis"

p = runAwait(Hello,"Hello")
print(p)
