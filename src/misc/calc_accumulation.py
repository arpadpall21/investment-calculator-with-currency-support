def cacl_accumulation_in_output_currency(
    accumulation: dict,
    exchange_rate: dict,
    output_currency: str
) -> float:
    result = 0

    for currency, val in accumulation.items():
        if currency == output_currency:
            result += val
            continue
        if not exchange_rate.get(currency):
            raise ValueError(f"Exchange rate missing for currency {currency}")
        result += val / exchange_rate[currency]

    return result
