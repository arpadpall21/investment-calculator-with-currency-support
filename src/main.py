from tomllib import load


def read_input_toml(path: str):
    with open(path, 'br') as f:
        return load(f)


def calculate_investment():
    input = read_input_toml("./input.toml")
    displayed_decimal_length = input['settings']['displayed_decimal_length']
    sum = input["start_sum"]

    for currency, value in sum.items():
        print(f"Start Sum {currency}: {value}")

    for investment_year in range(1, input["years_to_invest"]['years'] + 1):
        print(f"\nReport at the end of year {investment_year}")
        yearly_accumulation = {}

        for currency, yearly_interest_rate in input["yearly_interest_rate"].items():
            print(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)")
            gained_as_interest = sum[currency] / 100 * yearly_interest_rate
            total_at_year_end = sum[currency] + gained_as_interest
            print(f"    Gained as interest: {round(gained_as_interest, displayed_decimal_length)} {currency}")

            yearly_accumulation[currency] = {}
            yearly_accumulation[currency]['gained_as_interest'] = gained_as_interest

            if input["yearly_investment"].get(currency):
                print(f"    Yearly investment: {input["yearly_investment"][currency]} {currency}")
                total_at_year_end_yearly_invest_inc = total_at_year_end + input["yearly_investment"][currency]
                print(
                    "    Total including yearly investment: " +
                    f"{round(total_at_year_end_yearly_invest_inc, displayed_decimal_length)} {currency}"
                )
                yearly_accumulation[currency]['total'] = total_at_year_end_yearly_invest_inc
                sum[currency] = total_at_year_end_yearly_invest_inc
            else:
                print(f"    Total: {round(total_at_year_end, displayed_decimal_length)} {currency}")
                yearly_accumulation[currency]['total'] = total_at_year_end
                sum[currency] = total_at_year_end

        print('---', yearly_accumulation)
        print(f"Total in target currency {input["output_curency"]}")
        print(f"    Gained as interest: {input["output_curency"]}")
        print(f"    Total: {input["output_curency"]}")


if __name__ == "__main__":
    calculate_investment()
