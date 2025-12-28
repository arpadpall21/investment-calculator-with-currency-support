from misc.input import input_toml


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
