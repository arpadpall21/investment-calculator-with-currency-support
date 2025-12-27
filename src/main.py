from misc.input import input_toml
from misc.calc_accumulation import to_output_currency
from misc.print import prt, fmt_float
from misc.models import Bank, Accumulator


def invest():
    output_currency: str = input_toml["output_currency"]
    bank: Bank = Bank()

    # start sum
    prt("Start sum:", color="yellow")
    for currency, value in input_toml["start_sum"].items():
        bank.per_currency[currency] = Accumulator(capital=value)
        bank.total_in_output_currency.capital += to_output_currency(value, currency)

        prt(f"{fmt_float(value)} {currency}", tabs=1)

    prt(
        f"Total in output currency: {fmt_float(bank.total_in_output_currency.capital)} {output_currency}",
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
        total_yearly_interest_in_output_currency: float = 0.0

        for currency, yearly_interest_rate in input_toml["yearly_interest_rate"].items():
            prt(f"Currency: {currency} (yearly interest rate: {yearly_interest_rate}%)", color="yellow")

            interest: float = bank.per_currency[currency].capital / 100 * yearly_interest_rate
            interest_in_output_currency: float = to_output_currency(interest, currency)

            bank.per_currency[currency].capital += interest
            bank.per_currency[currency].interest += interest
            bank.total_in_output_currency.capital += interest_in_output_currency
            bank.total_in_output_currency.interest += interest_in_output_currency
            total_yearly_interest_in_output_currency += interest_in_output_currency

            prt(f"Interest this year: {fmt_float(interest)} {currency}", tabs=1)
            prt(
                "Interest total: " +
                f"{fmt_float(bank.per_currency[currency].interest)} {currency}",
                tabs=1,
            )

            prt(f"Total: {fmt_float(bank.per_currency[currency].capital)} {currency}", tabs=2)

            if input_toml["yearly_investment"].get(currency):
                yearly_investment: float = input_toml["yearly_investment"][currency]
                bank.per_currency[currency].capital += yearly_investment
                bank.total_in_output_currency.capital += to_output_currency(yearly_investment, currency)

                prt(f"Yearly investment: {fmt_float(yearly_investment)} {currency}", tabs=1)
                prt(
                    "Total including yearly investment: " +
                    f"{fmt_float(bank.per_currency[currency].capital)} {currency}",
                    tabs=2,
                )

        prt(f"Total in output currency {output_currency}", color="green")   # TODO
        prt(
            f"Gained as interest this year: {fmt_float(total_yearly_interest_in_output_currency)} " +
            f"{output_currency}",
            tabs=1,
            color="green",
        )
        prt(
            f"Interest total: {fmt_float(bank.total_in_output_currency.interest)} {output_currency} ",
            tabs=1,
            color="green",
        )
        prt(
            f"Total: {fmt_float(bank.total_in_output_currency.capital)} {output_currency}",
            tabs=2,
            color="green",
        )


if __name__ == "__main__":
    invest()
