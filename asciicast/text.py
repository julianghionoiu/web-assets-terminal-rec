from colorama import Fore, Style


def newline() -> str:
    return "\r\n"


def console_arrow() -> str:
    return Fore.CYAN + "➜ " + Style.RESET_ALL


def red(text: str) -> str:
    return Fore.RED + text + Style.RESET_ALL


def green(text: str) -> str:
    return Fore.GREEN + text + Style.RESET_ALL


def dim(text: str) -> str:
    return Style.DIM + text + Style.RESET_ALL


def bright(text: str) -> str:
    return Style.BRIGHT + text + Style.RESET_ALL
