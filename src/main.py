from misc.toml_file_reader import read as read_toml_file
from misc.calc_accumulation import cacl_accumulation_in_output_currency


def calculate_investment():
    input = read_toml_file("./input.toml")
    total_accumulation: dict = {}
    displayed_decimal_length = input["settings"]["displayed_decimal_length"]

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
            print(f"    Gained as interest: {round(gained_as_interest, displayed_decimal_length)} {currency}")

            total_accumulation[currency] += gained_as_interest
            print(f"    Total: {round(total_accumulation[currency], displayed_decimal_length)} {currency}")

            if input["yearly_investment"].get(currency):
                print(f"    Yearly investment: {input["yearly_investment"][currency]} {currency}")
                total_accumulation[currency] += input["yearly_investment"][currency]
                print(
                    "    Total including yearly investment: " +
                    f"{round(total_accumulation[currency], displayed_decimal_length)} {currency}"
                )

        total_in_output_currency = cacl_accumulation_in_output_currency(total_accumulation,
                                                                        input["exchange_rate"],
                                                                        input["output_currency"])
        total_yearly_interest_in_output_currency = cacl_accumulation_in_output_currency(yearly_interest_accumulation,
                                                                                        input["exchange_rate"],
                                                                                        input["output_currency"])
        print(f"Total in output currency {input["output_currency"]}")
        print("    Gained as interest this year: " +
              f"{round(total_yearly_interest_in_output_currency, displayed_decimal_length)}"
              f" {input["output_currency"]}")
        print(f"    Total: {round(total_in_output_currency, displayed_decimal_length)} {input["output_currency"]}")


if __name__ == "__main__":
    calculate_investment()
