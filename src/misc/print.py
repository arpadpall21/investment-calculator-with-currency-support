from misc.settings import settings

text_color = {
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "magenta": "\x1b[35m"
}


def prt(msg: str, new_line: bool = False, tabs: int = 0, color: str = ""):
    new_line_prefix = "\n" if new_line else ""
    tab_prefix: str = " " * settings.tab_size * tabs

    if color:
        if not text_color.get(color):
            raise ValueError(f"Color not supported: \"{color}\"")

        print(f"{text_color[color]}{new_line_prefix + tab_prefix + msg}\033[0m")
        return

    print(f"{new_line_prefix + tab_prefix + msg}")


def fmt_float(nr: float) -> str:
    return f"{{:{settings.dig_gr_sep}}}".format(round(nr, settings.dec_len))
