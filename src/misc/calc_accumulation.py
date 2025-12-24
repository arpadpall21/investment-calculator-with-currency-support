from misc.input import input_toml


def to_output_currency(val: float, currency: str) -> float:
    if not input_toml["exchange_rate"].get(currency):
        raise ValueError(f"Exchange rate missing for currency {currency}")

    return val / input_toml["exchange_rate"][currency]
