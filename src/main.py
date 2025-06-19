from misc.input import input
from misc.calc_accumulation import calc_accumulation_in_output_currency
from misc.print import prt, fmt_float


def calculate_investment():
    total_accumulation: dict = {}

    for currency, value in input["start_sum"].items():
        prt(f"Start Sum {currency}: {value}")
        total_accumulation[currency] = value

    for investment_year in range(1, input["years_to_invest"]["years"] + 1):
        prt(f"Report at the end of year {investment_year}", new_line=True)
        yearly_interest_accumulation = {}

        for currency, yearly_interest_rate in input["yearly_interest_rate"].items():
            prt(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)")

            gained_as_interest: float = total_accumulation[currency] / 100 * yearly_interest_rate
            yearly_interest_accumulation[currency] = gained_as_interest
            prt(f"Gained as interest: {fmt_float(gained_as_interest)} {currency}", tabs=1)

            total_accumulation[currency] += gained_as_interest
            prt(f"Total: {fmt_float(total_accumulation[currency])} {currency}", tabs=1)

            if input["yearly_investment"].get(currency):
                prt(f"Yearly investment: {input["yearly_investment"][currency]} {currency}", tabs=1)
                total_accumulation[currency] += input["yearly_investment"][currency]
                prt(f"Total including yearly investment: {fmt_float(total_accumulation[currency])} {currency}", tabs=1)

        total_in_output_currency = calc_accumulation_in_output_currency(total_accumulation)
        total_yearly_interest_in_output_currency = calc_accumulation_in_output_currency(yearly_interest_accumulation)
        prt(f"Total in output currency {input["output_currency"]}")
        prt(f"Gained as interest this year: {fmt_float(total_yearly_interest_in_output_currency)}" +
            f" {input["output_currency"]}", tabs=1)
        prt(f"Total: {fmt_float(total_in_output_currency)} {input["output_currency"]}", tabs=1)


if __name__ == "__main__":
    calculate_investment()
