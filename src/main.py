from tomllib import load


def read_input_toml(path: str):
    with open(path, 'br') as f:
        return load(f)


def calculate_investment():
    input = read_input_toml('./input.toml')

    for currency, value in input['start_sum'].items():
        print(f"Initial sum {currency}: {value}")


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
