def cacl_accumulation_in_output_currency(
    accumulation: dict,
    exchange_rate: dict,
    output_currency: str
) -> tuple[float, float]:
    total_interest = 0
    total = 0

    for currency, report in accumulation.items():
        if currency == output_currency:
            total_interest += report["gained_as_interest"]
            total += report["total"]
            continue

        if not exchange_rate.get(currency):
            raise ValueError(f"Exchange rate missing for currency {currency}")

        total_interest += report["gained_as_interest"] / exchange_rate[currency]
        total += report["total"] / exchange_rate[currency]

    return total_interest, total
