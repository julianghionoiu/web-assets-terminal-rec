def console_arrow() -> str:
    return "\u001b[36m➜ \u001b[m"


def newline() -> str:
    return "\r\n"


# ~~~~~~~~~~ Colours

def red(text: str) -> str:
    return "\u001b[31m{}\u001b[0m".format(text)


def green(text: str) -> str:
    return "\u001b[32m{}\u001b[0m".format(text)


def dim(text: str) -> str:
    return "\u001b[2m{}\u001b[0m".format(text)


def bright(text: str) -> str:
    return "\u001b[1m{}\u001b[0m".format(text)


# ~~~~~~~~~~ Utils

def trim(text: str, length: int):
    return (text[:20] + '..') if len(text) > length else text


def replace_escapes(text: str):
    return text.replace("\u001b", "Esc")
