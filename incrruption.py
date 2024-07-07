# importing modules that are needed
from modules import *
import pyfiglet
from colorama import Fore, Style
from os import system as run

# format as short
format = pyfiglet.figlet_format

# defining colores in short
red = Fore.RED
blue = Fore.BLUE
black = Fore.BLACK
green = Fore.GREEN
reset = Style.RESET_ALL

# options menu
options = """
[0] Exit
[1] Encrypt Image 
[2] Decrypt Image
"""

# choices to select
choice_options = "choose [ 1 / 2 / 0 (exit)] : "

# menu method
def menu():
    print(green+options+reset)
    choice = int(input(blue+choice_options+reset))
    return choice

# banner method that shows the tool name and
def banner():
    print(blue+format("InCorruption")+reset)
    print(red+"--------------------------------------------------------------"+reset)

# main method where all the methods are collected and shown
def main():
    try:
        choice = menu()
        if choice == 1:
            path = input("Enter image path : ")
            key = int(input("Enter secret key (numbers only) : "))
            encrypt_image(path, key)
        elif choice == 2:
            path = input("Enter image path : ")
            key = int(input("Enter secret key (numbers only) : "))
            decrypt_image(path, key)
        else:
            print("Exiting script ! Bye !")
            run("exit")
    except:
        print("Exiting script ! Bye !")
        run("exit")

# calling the banner and main method
if __name__ == "__main__":
    banner()
    main()