from misc.input import input_toml
from misc.calc_accumulation import to_output_currency
from misc.print import prt, fmt_float
from misc.models import Accumulator


def invest():
    output_currency: str = input_toml["output_currency"]
    accumulator: Accumulator = Accumulator()
    
    
    accumulation: dict = {"total_in_output_currency": 0, "accumulated_interest_in_output_currency": 0}
    yearly_interest_accumulator = {"total_in_output_currency": 0}


    # start sum
    prt("Start sum:", color="yellow")
    for currency, value in input_toml["start_sum"].items():
        accumulation[currency] = {"total": value, "accumulated_interest": 0}
        val_in_output_currency: float = to_output_currency(value, currency)
        accumulator.total_start_sum_in_output_currency += val_in_output_currency
        accumulator.total_end_sum_in_output_currency += val_in_output_currency
        prt(f"{fmt_float(value)} {currency}", tabs=1)

    prt(f"Total in output currency: {fmt_float(accumulator.total_start_sum_in_output_currency)}", color="green", tabs=2)

    # investment per year
    if len(input_toml["yearly_investment"]) > 0:
        prt("Yearly investment:", color="yellow")
        total_yearly_investment_in_output_currency: float = 0

        for currency, value in input_toml["yearly_investment"].items():
            total_yearly_investment_in_output_currency += to_output_currency(value, currency)
            prt(f"{fmt_float(value)} {currency}", tabs=1)

        prt(
            f"Total in output currency: {fmt_float(total_yearly_investment_in_output_currency)}",
            color="green",
            tabs=2,
        )

    # yearly interest calc
    for investment_year in range(1, input_toml["years_to_invest"]["years"] + 1):
        prt(f"Report at the end of year {investment_year}", new_line=True, color="magenta")

        for currency, yearly_interest_rate in input_toml["yearly_interest_rate"].items():
            prt(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)", color="yellow")

            gained_as_interest_this_year: float = accumulation[currency]["total"] / 100 * yearly_interest_rate
            interest_in_output_currency: float = to_output_currency(
                gained_as_interest_this_year, currency,
            )
            accumulator.total_end_sum_in_output_currency += interest_in_output_currency
            accumulator.total_accumulated_interest_in_output_currency += interest_in_output_currency
            
            

            if yearly_interest_accumulator.get(currency) is None:
                yearly_interest_accumulator[currency] = 0
            yearly_interest_accumulator[currency] += gained_as_interest_this_year

            prt(f"Gained as interest this year: {fmt_float(gained_as_interest_this_year)} {currency}", tabs=1)
            prt(f"Gained as interest from start: {fmt_float(yearly_interest_accumulator[currency])} {currency}", tabs=1)

            accumulation[currency]["total"] += gained_as_interest_this_year
            accumulation[currency]["accumulated_interest"] = gained_as_interest_this_year
            gained_as_interest_this_year_in_output_currency = to_output_currency(
                gained_as_interest_this_year,
                currency
            )
            accumulator.total_end_sum_in_output_currency += gained_as_interest_this_year_in_output_currency
            accumulator.total_accumulated_interest_in_output_currency += gained_as_interest_this_year_in_output_currency

            prt(f"Total: {fmt_float(accumulation[currency]["total"])} {currency}", tabs=2)

            if input_toml["yearly_investment"].get(currency):
                yearly_investment: float = input_toml["yearly_investment"][currency]

                accumulation[currency]["total"] += yearly_investment
                accumulator.total_start_sum_in_output_currency += to_output_currency(yearly_investment, currency)

                prt(f"Yearly investment: {fmt_float(yearly_investment)} {currency}", tabs=1)
                prt(
                    f"Total including yearly investment: {fmt_float(accumulation[currency]["total"])} {currency}",
                    tabs=2,
                )

        prt(f"Total in output currency {output_currency}", color="green")
        # prt(      # TODO...
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
            f"Total: {fmt_float(accumulator.total_end_sum_in_output_currency)} {output_currency}",
            tabs=2,
            color="green",
        )


if __name__ == "__main__":
    invest()
