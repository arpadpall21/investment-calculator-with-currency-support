from dataclasses import dataclass


@dataclass
class Accumulator:
    total_start_sum_in_output_currency: float = 0
    total_end_sum_output_currency: float = 0
    accumulated_interest_in_output_currency: float = 0
