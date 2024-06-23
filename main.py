import time, os

#Color codes
clear = '\x1b[0m'
red = '\x1b[31m'
cyan = '\x1b[96m'
bold = '\x1b[1m'
magenta = '\033[35m'

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
    return str(get_output('sh scripts/cpu.sh'))

def mumble_status():
    if get_output('sh scripts/mumble.sh') == 'running':
        return 'Running'
    else:
        return 'u dun goofed'
if __name__ == '__main__':
    while True:
        os.system('clear')
        print(bold + red + "RAM Usage:" + clear + bold)
        print(ram())
        print('\n' + cyan + "CPU Usage:" + clear + bold)
        print(cpu())
        print('\n' + magenta + "Mumble Status:" + clear + bold)
        print(mumble_status())


        time.sleep(5) #refresh rate