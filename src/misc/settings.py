from misc.toml_file_reader import read as read_toml_file

input = read_toml_file("./input.toml")
input_settings = input["settings"]


class Settings:
    dec_len = input_settings["displayed_decimal_length"]
    dig_gr_sep = input_settings["digit_grouping_separator"]


settings = Settings()
