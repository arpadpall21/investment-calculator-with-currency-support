from misc.input import input_toml
from misc.settings import settings

TEXT_COLOR: dict[str, str] = {
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "magenta": "\x1b[35m"
}


def prt(msg: str, new_line: bool = False, tabs: int = 0, color: str = ""):
    new_line_prefix = "\n" if new_line else ""
    tab_prefix: str = " " * settings.tab_size * tabs

    if color:
        if not TEXT_COLOR.get(color):
            raise ValueError(f"Color not supported: \"{color}\"")

        print(f"{TEXT_COLOR[color]}{new_line_prefix + tab_prefix + msg}\033[0m")
        return

    print(f"{new_line_prefix + tab_prefix + msg}")


def to_output_currency(val: float, currency: str) -> float:
    exchange_rate: float = 0.0
    if currency == input_toml["output_currency"]:
        exchange_rate = 1.0
    else:
        _exchange_rate: float | None = input_toml["exchange_rate"].get(currency)
        if _exchange_rate is None:
            raise ValueError(f"Exchange rate missing for currency {currency}")
        exchange_rate = _exchange_rate

    return val / exchange_rate


def fmt_float(nr: float) -> str:
    return f"{{:{settings.dig_gr_sep}}}".format(round(nr, settings.dec_len))
