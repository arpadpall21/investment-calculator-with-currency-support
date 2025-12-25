from dataclasses import dataclass, field


@dataclass
class YearlyAccumulator:
    interest_in_output_currency: float = 0


@dataclass
class Accumulator:
    total_start_sum_in_output_currency: float = 0
    total_end_sum_in_output_currency: float = 0
    total_accumulated_interest_in_output_currency: float = 0
    yearly: YearlyAccumulator = field(default_factory=YearlyAccumulator)
