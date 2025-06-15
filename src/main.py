from tomllib import load


def read_input_toml(path: str):
    with open(path, 'br') as f:
        return load(f)


def calculate_investment():
    input = read_input_toml('./input.toml')
    print(input)


if __name__ == "__main__":
    calculate_investment()
