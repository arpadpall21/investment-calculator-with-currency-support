from tomllib import load
from misc.calc_accumulation import cacl_accumulation_in_output_currency


def read_input_toml(path: str):
    with open(path, "br") as f:
        return load(f)


def calculate_investment():
    input = read_input_toml("./input.toml")
    total_accumulation: dict = {}
    displayed_decimal_length = input["settings"]["displayed_decimal_length"]

    for currency, value in input["start_sum"].items():
        print(f"Start Sum {currency}: {value}")
        total_accumulation[currency] = {"gained_as_interest": 0, "total": input["start_sum"][currency]}

    for investment_year in range(1, input["years_to_invest"]["years"] + 1):
        print(f"\nReport at the end of year {investment_year}")

        for currency, yearly_interest_rate in input["yearly_interest_rate"].items():
            print(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)")
            gained_as_interest: float = total_accumulation[currency]["total"] / 100 * yearly_interest_rate
            print(f"    Gained as interest: {round(gained_as_interest, displayed_decimal_length)} {currency}")

            total_accumulation[currency]["gained_as_interest"] += gained_as_interest
            total_accumulation[currency]["total"] += gained_as_interest
            print(f"    Total: {round(total_accumulation[currency]["total"], displayed_decimal_length)} {currency}")

            if input["yearly_investment"].get(currency):
                print(f"    Yearly investment: {input["yearly_investment"][currency]} {currency}")
                total_accumulation[currency]["total"] += input["yearly_investment"][currency]
                print(
                    "    Total including yearly investment: " +
                    f"{round(total_accumulation[currency]["total"], displayed_decimal_length)} {currency}"
                )

        gained_as_interest_yearly, total_yearly = cacl_accumulation_in_output_currency(total_accumulation,
                                                                                       input["exchange_rate"],
                                                                                       input["output_currency"])
        print(f"Total in output currency {input["output_currency"]}")
        print(f"    Gained as interest: {round(gained_as_interest_yearly, displayed_decimal_length)}" +
              f"{input["output_currency"]}")
        print(f"    Total: {round(total_yearly, displayed_decimal_length)} {input["output_currency"]}")

    print(total_accumulation)


if __name__ == "__main__":
    calculate_investment()
