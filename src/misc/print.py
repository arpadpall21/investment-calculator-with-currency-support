from enum import Enum
from misc.settings import settings


class TextColor(Enum):
    WHITE = "\x1b[37m"
    GREEN = "\x1b[32m"


class TextStyle(Enum):
    RESET = "\x1b[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class BackgroundColor(Enum):
    BLACK = "\x1b[40m"
    RED = "\x1b[41m"


def color_print(
    message: str,
    text_color: TextColor = TextColor.WHITE,
    text_style: TextStyle = TextStyle.RESET,
    background_color: BackgroundColor = BackgroundColor.BLACK
):
    end = "\033[0m"
    print(f"{text_color} {message}{end}")


def prt(msg: str, new_line: bool = False, tabs: int = 0):
    new_line_prefix = "\n" if new_line else ""
    tab_prefix: str = " " * settings.tab_size * tabs

    print(new_line_prefix + tab_prefix + msg)


def fmt_float(nr: float) -> str:
    return f"{{:{settings.dig_gr_sep}}}".format(round(nr, settings.dec_len))
