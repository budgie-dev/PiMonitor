import os, time

#Color codes
clear = '\x1b[0m'
red = '\x1b[31m'
cyan = '\x1b[96m'
bold = '\x1b[1m'
magenta = '\033[35m'
green = '\033[32m'

def get_output(command):
        result = os.popen(command)
        output = result.read().strip()
        return output

def ram():
    ramfree = get_output('sh scripts/ramfree.sh')
    ramtotal = get_output('sh scripts/ramtotal.sh')
    ramfree = int(ramtotal) - int(ramfree)
    return str((int(ramfree / int(ramtotal) * 100))) + "%"

def cpu():
    return str(100 - int(get_output('sh scripts/cpu.sh'))) + '%'

def temp():
    return str(get_output('sh scripts/temp.sh'))

def mumble_status():
    if get_output('sh scripts/mumble.sh') == 'running':
        return 'Running'
    else:
        return 'u dun goofed'
if __name__ == '__main__':
    while True:
        os.system('clear')
        print(bold + green + "   .~~.   .~~.       " + red + "RAM Usage:")
        print(green + "  '. \ ' ' / .'      " + clear + ram())
        print(red + "   .~ .~~~..~.       ")
        print(red + "  : .~.'~'.~. :      " + bold + magenta + "Minecraft Status:" + clear)
        print(red + " ~ (   ) (   ) ~     " + clear + mumble_status())
        print(red + "( : '~'.~.'~' : )    ")
        print(red + " ~ .~ (   ) ~. ~     " + bold + green + "CPU Core 0 temp:" + clear)
        print(red + "  (  : '~' :  )      " + clear + temp())
        print(red + "   '~ .~~~. ~'       ")
        print(red + "       '~'           " + bold + cyan + "CPU Usage:" + clear)
        print("                     " + clear + cpu())
        time.sleep(20) #refresh rate
