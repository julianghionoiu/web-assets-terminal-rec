def console_arrow() -> str:
    return "\u001b[36m➜ \u001b[m"


def thumbs_up() -> str:
    # Find code here: https://unicode.org/emoji/charts/full-emoji-list.html#1f44d
    # Get Java reference here: http://www.fileformat.info/info/unicode/char/1f44d/index.htm
    return "\uD83D\uDC4D"


def newline() -> str:
    return "\r\n"


# ~~~~~~~~~~ Colours

def black(text: str) -> str:
    return _color(30, text)


def red(text: str) -> str:
    return _color(31, text)


def green(text: str) -> str:
    return _color(32, text)


def yellow(text: str) -> str:
    return _color(33, text)


def blue(text: str) -> str:
    return _color(34, text)


def magenta(text: str) -> str:
    return _color(35, text)


def cyan(text: str) -> str:
    return _color(36, text)


def white(text: str) -> str:
    return _color(37, text)


def bright(text: str) -> str:
    return _color(1, text)


def dim(text: str) -> str:
    return _color(2, text)


def _color(code: int, text: str):
    return "\u001b[{}m{}\u001b[0m".format(code, text)


# ~~~~~~~~~~ Utils

def trim(text: str, length: int):
    return (text[:20] + '..') if len(text) > length else text


def replace_escapes(text: str):
    return text.replace("\u001b", "Esc")
