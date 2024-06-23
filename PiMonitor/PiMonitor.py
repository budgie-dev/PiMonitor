import os

def getoutput(command):
    result = os.popen(command)
    output = result.read().strip()
    return output

while True:
    #Cpu stats
    cpu =  getoutput('sh scripts/cpu.sh')
    
    #Ram stats
    ramfree = getoutput('sh scripts/ramfree.sh')
    ramtotal = getoutput('sh scripts/ramtotal.sh')
    ramfree =  int(ramtotal) - int(ramfree)
    print(str((int(ramfree / int(ramtotal) * 100))) + "%")