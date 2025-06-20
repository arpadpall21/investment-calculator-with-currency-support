from misc.input import input

input_settings = input["settings"]


class Settings:
    dec_len = input_settings["displayed_decimal_length"]
    dig_gr_sep = input_settings["digit_grouping_separator"]
    tab_size = input_settings["tab_size"]


settings = Settings()
