import os, time

#Color codes
clear = '\x1b[0m'
red = '\x1b[31m'
cyan = '\x1b[96m'
bold = '\x1b[1m'

def getoutput(command):
    result = os.popen(command)
    output = result.read().strip()
    return output

while True:
    #Cpu stats
    cpu = getoutput('sh scripts/cpu.sh')
    
    #Ram stats
    ramfree = getoutput('sh scripts/ramfree.sh')
    ramtotal = getoutput('sh scripts/ramtotal.sh')
    ramfree = int(ramtotal) - int(ramfree)
    print(bold + red + 'RAM Usage: ' + clear + str((int(ramfree / int(ramtotal) * 100))) + "%")
    time.sleep(1)
    os.system('clear')