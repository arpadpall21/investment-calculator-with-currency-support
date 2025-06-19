from tomllib import load


def read(path: str):
    with open(path, "br") as f:
        return load(f)
