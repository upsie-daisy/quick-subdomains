##################
#
# A Handy Script to Parse Command-Line Arguments
#
# github.com/upsie-daisy/quick-flags
# Made by @Upsie-Daisy
#
#################

import sys
from .tables import Table
from .ansi import a

class Flag:

    def __init__(self, description="", flags=[]): 
        self.description = description
        self.flags = flags
    
    class flag:
        def __init__(self, short="", full="", default=None, type="string", required=False, help=""):
            self.name = full.replace('-','')
            self.short = short
            self.full = full
            self.default = default
            self.type = type
            self.required = required
            self.help = help
            
    def new(self, short="", full="", default="", type="string", required=False, help=""):
        
        if full == "":
            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Long option required.")
            sys.exit(1)
        
        if type != "bool" and default == None and required == False:
            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Default value required for {full}.")
            sys.exit(1)
    
        self.flags.append(self.flag(short, full, default, type, required, help))
                
    def parse(self):
        for flag in self.flags:
            setattr(self, flag.full.replace('-',''), flag.default)
        
        argc = len(sys.argv)
        i = 1
        while i < argc:
            for flag in self.flags:
                found = False
                if sys.argv[i] == flag.short or sys.argv[i] == flag.full:
                    if flag.type == "bool":
                        setattr(self, flag.full.replace('-',''), True)
                    
                    elif flag.type == "int":
                        i += 1
                        if i >= argc:
                            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Missing \"int\" argument for \"{flag.full}\".")
                            sys.exit(1)
                        setattr(self, flag.full.replace('-',''), int(sys.argv[i]))

                    else: # Consider as string
                        i += 1
                        if i >= argc:
                            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Missing \"string\" argument for \"{flag.full}\".")
                            sys.exit(1)
                        setattr(self, flag.full.replace('-',''), sys.argv[i])
                    
                    flag.required = False
                    found = True
                    break
                
                elif sys.argv[i] == "-h" or sys.argv[i] == "--help":
                    print(f"{a.bl}[{a.g}?{a.bl}] {a.bl}Help: {a.rst}{self.description}.")
                    th = Table(spacer=True, style="=", border_color="black")
                    th.add(["", "Option", "Description", "Default"])
                    for flag in self.flags:
                        th.add([flag.short, flag.full, flag.help, flag.default])
                    th.draw()
                    sys.exit(0)
                    
            if found == False:
                print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}\"{sys.argv[i]}\" unknown.")
                sys.exit(1)
                
            i += 1
            
        for flag in self.flags:
            if flag.required == True:
                print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}\"{flag.full}\" is required.")
                sys.exit(1)