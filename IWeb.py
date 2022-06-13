import Admin_finder
from colorama import Fore, Back, Style
import os
import baners
import time
baners.Finder()

tools = """
[1] Admin FInder : 
[2] Soon . . . : 
"""
print(tools)

get_number =(input(Fore.BLUE + "Enter Number : "))

#Admin_Finder
#-----------------------------------------------------------------------------------------------------------
try:
    if get_number == "1":
        os.system("clear")
        print(Fore.RED +"https://web.com")
        print(Fore.YELLOW + ">>>Required Libraries , colorama , requests , time , os ")
        Admin_finder.Finder(input("Enter Web : "))
    elif get_number == "2":
        print("Soon Broo . . .")
        time.sleep(0.4)
        os.system("python3 IWeb.py")
except:
    print("invalid url ! ! !")
#-----------------------------------------------------------------------------------------------------------

#IP_information

