import pyautogui as spam
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.LIGHTMAGENTA_EX + """
              
           
                           ad888888b,  88                                     
                          d8"     "88  88                                     
                                  a8P  88                                     
8b,dPPYba,   8b       d8       aad8"   88           8b,     ,d8  8b,     ,d8  
88P'    "8a  `8b     d8'       ""Y8,   88            `Y8, ,8P'    `Y8, ,8P'   
88       d8   `8b   d8'           "8b  88              )888(        )888(     
88b,   ,a8"    `8b,d8'    Y8,     a88  88            ,d8" "8b,    ,d8" "8b,   
88`YbbdP"'       Y88'      "Y888888P'  88888888888  8P'     `Y8  8P'     `Y8  
88               d8'                                                          
88              d8'                                                           
                                                                                                                                 
    

          Spam: {}           {}by {}@EgeLord\n  """
      
      )


    


limit = input(Fore.LIGHTBLUE_EX + "Ne Kadar Gondermek Istersin:")
msg = input(Fore.LIGHTYELLOW_EX + "Ne Gondereceksın:")



i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

    i+=1

