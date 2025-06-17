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

        for currency, yearly_interest_rate in input["yearly_interest_rate"].items():
            print(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)")
            gained_as_interest = sum[currency] / 100 * yearly_interest_rate
            total_at_year_end = sum[currency] + gained_as_interest

            print(f"    Gained as interest: {round(gained_as_interest, displayed_decimal_length)}")

            if input["yearly_investment"].get(currency):
                print(f"    Yearly investment: {input["yearly_investment"][currency]}")

                total_at_year_end_yearly_invest_inc = total_at_year_end + input["yearly_investment"][currency]
                print(
                    "    Total sum at the end of the year including yearly investment: " +
                    f"{round(total_at_year_end_yearly_invest_inc, displayed_decimal_length)}"
                )
                sum[currency] = total_at_year_end_yearly_invest_inc
            else:
                print(f"    Total sum at the end of the year: {round(total_at_year_end, displayed_decimal_length)}")
                sum[currency] = total_at_year_end


        # print(f"Yearly report in target currency ({input["output_curency"]})")


if __name__ == "__main__":
    calculate_investment()


# monthly_investment_huf = 700_000
# initial_huf = 24_453_000 + 719618
# initial_ron = 152_634 + 318_000

# huf_exchange_rate = 0.0025
# ron_exchange_rate = 0.20

# current_total_eur = (initial_huf * huf_exchange_rate) + (initial_ron * ron_exchange_rate)
# yearly_investment_eur = monthly_investment_huf * huf_exchange_rate * 12

# print(f'Current total EUR: {current_total_eur}')
# print(f'Yearly investment EUR: {yearly_investment_eur}')


# def calc_investment(initial_sum, interest_rate, years, yearly_investment=0):
#     result = initial_sum

#     for year in range(years):
#         current_interest = result / 100 * interest_rate
#         print(f'Interest in year {year + 1}: {current_interest}')

#         result = result + current_interest + yearly_investment

#     return result


# print(f'Result: {calc_investment(current_total_eur, 5, 20, yearly_investment_eur)}')
