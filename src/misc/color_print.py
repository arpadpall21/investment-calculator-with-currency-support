class TextColor:
    WHITE = "\x1b[37m "
    GREEN = "\x1b[32m"


class TextStyle:
    RESET = "\x1b[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class BackgroundColor:
    Black = "\x1b[40m"
    RED = "\x1b[41m"


def color_print(message: str, text_color: TextColor, text_style: TextStyle, background_color: BackgroundColor):
    end = "\033[0m"
    print(text_color + " " + text_style + background_color + message + end)
