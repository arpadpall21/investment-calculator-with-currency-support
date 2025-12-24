from misc.input import input_toml
from misc.calc_accumulation import to_output_currency
from misc.print import prt, fmt_float


def invest():
    accumulation: dict = {"total_in_output_currency": 0, "accumulated_interest_in_output_currency": 0}
    total_start_sum_in_output_currency: float = 0

    prt("Start sum:", color="yellow")
    for currency, value in input_toml["start_sum"].items():
        accumulation[currency] = {"total": value, "accumulated_interest": 0}
        total_start_sum_in_output_currency += to_output_currency(value, currency)
        prt(f"{fmt_float(value)} {currency}", tabs=1)

    accumulation["total_in_output_currency"] += total_start_sum_in_output_currency
    prt(f"Total in output currency: {fmt_float(total_start_sum_in_output_currency)}", color="green", tabs=2)

    if len(input_toml["yearly_investment"]) > 0:
        prt("Yearly investment:", color="yellow")
        total_start_yearly_investment_in_output_currency: float = 0

        for currency, value in input_toml["yearly_investment"].items():
            total_start_yearly_investment_in_output_currency += to_output_currency(value, currency)
            prt(f"{fmt_float(value)} {currency}", tabs=1)

        prt(
            f"Total in output currency: {fmt_float(total_start_yearly_investment_in_output_currency)}",
            color="green",
            tabs=2,
        )

    for investment_year in range(1, input_toml["years_to_invest"]["years"] + 1):
        prt(f"Report at the end of year {investment_year}", new_line=True, color="magenta")
        yearly_interest_accumulation = {}

        for currency, yearly_interest_rate in input_toml["yearly_interest_rate"].items():
            prt(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)", color="yellow")

            gained_as_interest_this_year: float = accumulation[currency]["total"] / 100 * yearly_interest_rate
            yearly_interest_accumulation[currency] = gained_as_interest_this_year
            prt(f"Gained as interest this year: {fmt_float(gained_as_interest_this_year)} {currency}", tabs=1)

            accumulation[currency]["total"] += gained_as_interest_this_year
            accumulation[currency]["accumulated_interest"] = gained_as_interest_this_year
            gained_as_interest_this_year_in_output_currency = to_output_currency(
                gained_as_interest_this_year,
                currency
            )
            accumulation["total_in_output_currency"] += gained_as_interest_this_year_in_output_currency
            accumulation["accumulated_interest_in_output_currency"] += gained_as_interest_this_year_in_output_currency

            prt(f"Total: {fmt_float(accumulation[currency]["total"])} {currency}", tabs=2)

            if input_toml["yearly_investment"].get(currency):
                accumulation[currency]["total"] += input_toml["yearly_investment"][currency]
                accumulation["total_in_output_currency"] += to_output_currency(
                    input_toml["yearly_investment"][currency],
                    currency,
                )

                prt(f"Yearly investment: {fmt_float(input_toml["yearly_investment"][currency])} {currency}", tabs=1)
                prt(
                    f"Total including yearly investment: {fmt_float(accumulation[currency]["total"])} {currency}",
                    tabs=2,
                )

        interest_from_start_in_output_currency: float = accumulation["accumulated_interest_in_output_currency"]
        interest_from_start_in_percent: float = fmt_float(
            interest_from_start_in_output_currency / total_start_sum_in_output_currency * 100
        )
        prt(f"Total in output currency {input_toml["output_currency"]}", color="green")
        prt(
            "Gained as interest from start: " +
            f"{fmt_float(interest_from_start_in_output_currency)} {input_toml["output_currency"]} " +
            f"({interest_from_start_in_percent}%)",
            tabs=1,
            color="green",
        )
        prt(
            f"Total: {fmt_float(accumulation["total_in_output_currency"])} {input_toml["output_currency"]}",
            tabs=2,
            color="green",
        )


if __name__ == "__main__":
    invest()
