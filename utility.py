import os
def draw_logo():
    print(r'''
 
 __ _ _   _  ___  ___ ___  
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/            
          

          ''')

def clear_screen():
    os.system("cls")  
    draw_logo()  