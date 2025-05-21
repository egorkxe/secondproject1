from colorama import init, Fore, Back, Style

init()

print(Fore.RED + 'Це червоний текст')
print(Fore.GREEN + 'Це зелений текст')
print(Fore.YELLOW + 'Це жовтий текст')
print(Fore.BLUE + 'Це синій текст')


print(Back.RED + 'Це текст на червоному фоні' + Back.RESET)
print(Back.GREEN + 'Це текст на зеленому фоні' + Back.RESET)

print(Style.BRIGHT + Fore.CYAN + Back.BLACK + 'Яскравий бірюзовий текст на чорному фоні' + Style.RESET_ALL)
