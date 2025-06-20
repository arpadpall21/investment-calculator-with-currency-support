from misc.settings import settings

color = {
    "text": {
        "white": "\x1b[37m",
        "green": "\x1b[32m",
    },
    "background": {
        "black": "\x1b[40m",
        "red": "\x1b[41m",
    },
}


def prt(msg: str, new_line: bool = False, tabs: int = 0, text_color: str = "white", bg_color: str = "black"):
    new_line_prefix = "\n" if new_line else ""
    tab_prefix: str = " " * settings.tab_size * tabs
    text_color = color["text"][text_color]
    bg_color = color["background"][bg_color]
    end = "\033[0m"

    print(f"{text_color}{new_line_prefix + tab_prefix + msg}{end}")


def fmt_float(nr: float) -> str:
    return f"{{:{settings.dig_gr_sep}}}".format(round(nr, settings.dec_len))
