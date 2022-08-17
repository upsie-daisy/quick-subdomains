##################
#
# A Handy Script to Use ANSI Escape Sequences
# This is the short text version, faster to type but harder to remember
#
# github.com/upsie-daisy/quick-ansi
# Made by @Upsie-Daisy
#
#################

class a:
    ### Text styling
    rst = '\033[0m' # reset
    bld = '\033[1m' # bold
    fnt = '\033[2m' # faint
    itc = '\033[3m' # italic
    udr = '\033[4m' # underline
    sbk = '\033[5m' # slow blink
    rbk = '\033[6m' # rapid blink
    rvs = '\033[7m' # reverse
    con = '\033[8m' # conceal
    crs = '\033[9m' # crossed out
    dft = '\033[10m' # default
    fra = '\033[20m' # fraktur
    
    # Foreground colors
    class br: # Bright
        bl = '\033[90m' # black
        r = '\033[91m' # red
        g = '\033[92m' # green
        y = '\033[93m' # yellow
        b = '\033[94m' # blue
        m = '\033[95m' # magenta
        c = '\033[96m' # cyan
        w = '\033[97m' # white
        
    bl = '\033[30m' # black
    r = '\033[31m' # red
    g = '\033[32m' # green
    y = '\033[33m' # yellow
    b = '\033[34m' # blue
    m = '\033[35m' # magenta
    c = '\033[36m' # cyan
    w = '\033[37m' # white

    # Background colors
    class bck:
        class br: # bright
            bl = '\033[100m' # black
            r = '\033[101m' # red
            g = '\033[102m' # green
            y = '\033[103m' # yellow
            b = '\033[104m' # blue
            m = '\033[105m' # magenta
            c = '\033[106m' # cyan
            w = '\033[107m' # white

        bl = '\033[40m' # black
        r = '\033[41m' # red
        g = '\033[42m' # green
        y = '\033[43m' # yellow
        b = '\033[44m' # blue
        m = '\033[45m' # magenta
        c = '\033[46m' # cyan
        w = '\033[47m' # white  
    
    # Others
    clr = '\033[2J' # clear screen
    cll = '\033[2K' # clear line
    cel = '\033[K' # clear to end of line
    
    # Save and restore cursor position
    sc = '\033[s' # save cursor position
    rc = '\033[u' # restore cursor position
    
    def m(l,c): # move to line l and column c
        return f"\033[{l};{c}H"
    def mu(n): # move up n line
        return f"\033[{n}A"
    def md(n): # move down n line
        return f"\033[{n}B"
    def mf(n): # move forward n char
        return f"\033[{n}C"
    def mb(n): # move backward n char
        return f"\033[{n}D"