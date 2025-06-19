from misc.input import input


def calc_accumulation_in_output_currency(accumulation: dict) -> float:
    result = 0

    for currency, val in accumulation.items():
        if currency == input["output_currency"]:
            result += val
            continue
        if not input["exchange_rate"].get(currency):
            raise ValueError(f"Exchange rate missing for currency {currency}")
        result += val / input["exchange_rate"][currency]

    return result
