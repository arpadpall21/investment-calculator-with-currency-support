from misc.input import input
from misc.calc_accumulation import calc_accumulation_in_output_currency
from misc.print import fmt_float


def calculate_investment():
    total_accumulation: dict = {}

    for currency, value in input["start_sum"].items():
        print(f"Start Sum {currency}: {value}")
        total_accumulation[currency] = value

    for investment_year in range(1, input["years_to_invest"]["years"] + 1):
        print(f"\nReport at the end of year {investment_year}")
        yearly_interest_accumulation = {}

        for currency, yearly_interest_rate in input["yearly_interest_rate"].items():
            print(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)")

            gained_as_interest: float = total_accumulation[currency] / 100 * yearly_interest_rate
            yearly_interest_accumulation[currency] = gained_as_interest
            print(f"    Gained as interest: {fmt_float(gained_as_interest)} {currency}")

            total_accumulation[currency] += gained_as_interest
            print(f"    Total: {fmt_float(total_accumulation[currency])} {currency}")

            if input["yearly_investment"].get(currency):
                print(f"    Yearly investment: {input["yearly_investment"][currency]} {currency}")
                total_accumulation[currency] += input["yearly_investment"][currency]
                print(
                    "    Total including yearly investment: " +
                    f"{fmt_float(total_accumulation[currency])} {currency}"
                )

        total_in_output_currency = calc_accumulation_in_output_currency(total_accumulation)
        total_yearly_interest_in_output_currency = calc_accumulation_in_output_currency(yearly_interest_accumulation)
        print(f"Total in output currency {input["output_currency"]}")
        print(f"    Gained as interest this year: {fmt_float(total_yearly_interest_in_output_currency)}"
              f" {input["output_currency"]}")
        print(f"    Total: {fmt_float(total_in_output_currency)} {input["output_currency"]}")


if __name__ == "__main__":
    calculate_investment()
