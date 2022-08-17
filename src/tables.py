##################
#
# A Handy Script to Draw ASCII Tables
#
# github.com/upsie-daisy/quick-tables
# Made by @Upsie-Daisy
#
#################

class Table:
    def __init__(self, style="-", data=[], spacer=True, border_color="black", text_color="white", align="left", max_length=30): 
        self.data = data
        self.style = style
        self.spacer = spacer
        self.border_color = border_color
        self.text_color = text_color
        self.align = align
        self.max_length = max_length
    
    def color(self, name):    
        if name == "red":
            return '\033[31m'
        elif name == "green":
            return '\033[32m'
        elif name == "yellow":
            return '\033[33m'
        elif name == "blue":
            return '\033[34m' 
        elif name == "magenta":
            return '\033[35m'
        elif name == "cyan":
            return '\033[36m' 
        elif name == "white":
            return '\033[37m'
        # Default : Black
        else:
            return '\033[30m'
    
    def add(self, data=[]):
        self.data.append(data)

    def draw(self):
        nrow = 0
        ncol = 0
        
        for row in self.data:
            nrow += 1
            if len(row) > ncol:
                ncol = len(row)
                        
        col_size = []
        for i in range(ncol):
            col_size.append(0)
            for row in self.data:
                try:
                    if len(row[i]) > col_size[i]:
                        if len(row[i]) > self.max_length:
                            row[i] = row[i][:self.max_length-2] + ".."
                        col_size[i] = len(row[i])
                except:
                    continue
        
        # Styling
        bg_color = self.color(self.border_color)
        text_color = self.color(self.text_color)   
         
        if self.style == "-":
            top_left = f"{bg_color}┌\033[0m"
            top_right = f"{bg_color}┐\033[0m"
            bottom_left = f"{bg_color}└\033[0m"
            bottom_right = f"{bg_color}┘\033[0m"
            to_left = f"{bg_color}┤\033[0m"
            to_right = f"{bg_color}├\033[0m"
            to_down = f"{bg_color}┬\033[0m"
            to_up = f"{bg_color}┴\033[0m"
            middle = f"{bg_color}┼\033[0m"
            verticaly = f"{bg_color}│\033[0m"
            horizontaly = f"{bg_color}─\033[0m"  
        elif self.style == "=":
            top_left = f"{bg_color}╔\033[0m"
            top_right = f"{bg_color}╗\033[0m"
            bottom_left = f"{bg_color}╚\033[0m"
            bottom_right = f"{bg_color}╝\033[0m"
            to_left = f"{bg_color}╣\033[0m"
            to_right = f"{bg_color}╠\033[0m"
            to_up = f"{bg_color}╩\033[0m"
            to_down = f"{bg_color}╦\033[0m"
            middle = f"{bg_color}╬\033[0m"
            verticaly = f"{bg_color}║\033[0m"
            horizontaly = f"{bg_color}═\033[0m"
        else:
            top_left = " "
            top_right = " "
            bottom_left = " "
            bottom_right = " "
            to_left = " "
            to_right = " "
            to_up = " "
            to_down = " "
            middle = " "
            verticaly = " "
            horizontaly = " "

        # Top row
        print(top_left,end="")
        for i in range(ncol-1):
            for j in range(col_size[i]+2):
                print(horizontaly, end="")
            print(to_down,end="")
        if ncol > 1:
            for j in range(col_size[i+1]+2):
                print(horizontaly, end="")
        else:
            for j in range(col_size[i]+2):
                print(horizontaly, end="")          
        print(top_right)
        
        # Write data
        crow = 1
        for row in self.data:
            i = 0
            for col in row:                    
                print(f"{verticaly} ", end="")
                print(text_color, end="")
                if self.align == "right":
                    for j in range(len(col), col_size[i]):
                        print(" ", end="")
                    print(f"{col} ", end="")
                
                elif self.align == "center":
                    for j in range(int((col_size[i]-len(col))/2)):    
                        print(" ", end="")
                    print(f"{col} ", end="")
                    if col_size[i] > 1:
                        for k in range(col_size[i]-len(col)-j-1):    
                            print(" ", end="") 
                else:
                    print(col, end="")
                    for j in range(len(str(col)), col_size[i]+1):
                        print(" ", end="")
                print('\033[0m', end="")

                i += 1
                
            for j in range(i, ncol):
                print(f"{verticaly} ", end="")
                for k in range(col_size[j]+1):
                    print(" ", end="")  
            print(verticaly)   

            # Spacers
            if self.spacer:
                if crow < nrow:
                    print(to_right,end="")
                    for i in range(ncol-1):
                        for j in range(col_size[i]+2):
                            print(horizontaly, end="")
                        print(middle,end="")
                    if ncol > 1:
                        for j in range(col_size[i+1]+2):
                            print(horizontaly, end="")
                    else:
                         for j in range(col_size[i-1]+2):
                                print(horizontaly, end="")                       
                    print(to_left)
            
            crow += 1  
        
        # Bottom row
        print(bottom_left,end="")
        for i in range(ncol-1):
            for j in range(col_size[i]+2):
                print(horizontaly, end="")
            print(to_up,end="")
        if ncol > 1:
            for j in range(col_size[i+1]+2):
                print(horizontaly, end="")
        else:
            for j in range(col_size[i-1]+2):
                print(horizontaly, end="")         
        print(bottom_right)