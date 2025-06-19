from tomllib import load


def read_toml_file(path: str):
    with open(path, "br") as f:
        return load(f)


input = read_toml_file("./input.toml")
