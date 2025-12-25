from misc.input import input_toml
from misc.calc_accumulation import to_output_currency
from misc.print import prt, fmt_float
from misc.models import Accumulator, AccumulatorPerCurrency


def invest():
    output_currency: str = input_toml["output_currency"]
    accumulator: Accumulator = Accumulator()

    # start sum
    prt("Start sum:", color="yellow")
    for currency, value in input_toml["start_sum"].items():
        sum_in_output_currency: float = to_output_currency(value, currency)

        accumulator.per_currency[currency] = AccumulatorPerCurrency(total_accumulated=value)
        accumulator.total_start_sum_in_output_currency += sum_in_output_currency
        accumulator.total_accumulated_in_output_currency += sum_in_output_currency

        prt(f"{fmt_float(value)} {currency}", tabs=1)

    prt(
        f"Total in output currency: {fmt_float(accumulator.total_start_sum_in_output_currency)} {output_currency}",
        color="green",
        tabs=2,
    )

    # investment per year
    if len(input_toml["yearly_investment"]) > 0:
        prt("Yearly investment:", color="yellow")
        total_yearly_investment_in_output_currency: float = 0

        for currency, value in input_toml["yearly_investment"].items():
            total_yearly_investment_in_output_currency += to_output_currency(value, currency)
            prt(f"{fmt_float(value)} {currency}", tabs=1)

        prt(
            f"Total in output currency: {fmt_float(total_yearly_investment_in_output_currency)} {output_currency}",
            color="green",
            tabs=2,
        )

    # yearly interest calc
    for investment_year in range(1, input_toml["years_to_invest"]["years"] + 1):
        prt(f"Report at the end of year {investment_year}", new_line=True, color="magenta")

        for currency, yearly_interest_rate in input_toml["yearly_interest_rate"].items():
            prt(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)", color="yellow")

            interest: float = accumulator.per_currency[currency].total_accumulated / 100 * yearly_interest_rate
            interest_in_output_currency: float = to_output_currency(interest, currency)

            accumulator.per_currency[currency].total_accumulated_interest += interest
            accumulator.per_currency[currency].total_accumulated += interest
            accumulator.total_accumulated_in_output_currency += interest_in_output_currency
            accumulator.total_accumulated_interest_in_output_currency += interest_in_output_currency

            prt(f"Gained as interest this year: {fmt_float(interest)} {currency}", tabs=1)
            prt(
                "Gained as interest from start: " +
                f"{fmt_float(accumulator.per_currency[currency].total_accumulated_interest)} {currency} " +
                f"({fmt_float(
                    accumulator.per_currency[currency].total_accumulated_interest / input_toml["start_sum"][currency] * 100
                )}%)",
                tabs=1,
            )

            prt(f"Total: {fmt_float(accumulator.per_currency[currency].total_accumulated)} {currency}", tabs=2)

            if input_toml["yearly_investment"].get(currency):
                yearly_investment: float = input_toml["yearly_investment"][currency]
                yearly_investment_in_output_currency: float = to_output_currency(yearly_investment, currency)

                accumulator.per_currency[currency].total_accumulated += yearly_investment
                accumulator.total_accumulated_in_output_currency += yearly_investment_in_output_currency

                prt(f"Yearly investment: {fmt_float(yearly_investment)} {currency}", tabs=1)
                prt(
                    "Total including yearly investment: " +
                    f"{fmt_float(accumulator.per_currency[currency].total_accumulated)} {currency}",
                    tabs=2,
                )

        prt(f"Total in output currency {output_currency}", color="green")
        # prt(    # TODO fix it
        #     f"Gained as interest this year: {fmt_float(accumulator.total_accumulated_interest_in_output_currency)} " +
        #     f"{output_currency}",
        #     tabs=1,
        #     color="green",
        # )
        prt(
            "Gained as interest from start: " +
            f"{fmt_float(accumulator.total_accumulated_interest_in_output_currency)} {output_currency} " +
            f"({fmt_float(
                accumulator.total_accumulated_interest_in_output_currency / accumulator.total_start_sum_in_output_currency * 100
            )}%)",
            tabs=1,
            color="green",
        )
        prt(
            f"Total: {fmt_float(accumulator.total_accumulated_in_output_currency)} {output_currency}",
            tabs=2,
            color="green",
        )


if __name__ == "__main__":
    invest()
