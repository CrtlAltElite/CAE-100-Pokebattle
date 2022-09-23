from colorama import Fore, Style, init

init()

print("hello")
print(Fore.YELLOW, end="")
print("Yellow Hello")
print(Style.BRIGHT, end="")
print("Bright Yellow Hello")
print(Style.RESET_ALL, end="")
print("be back to normal Hello")
