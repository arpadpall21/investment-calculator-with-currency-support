from dataclasses import dataclass, field


@dataclass
class AccumulatorPerCurrency:
    total_accumulated: float = 0.0
    total_accumulated_interest: float = 0.0


@dataclass
class Accumulator:
    total_start_sum_in_output_currency: float = 0.0
    total_accumulated_in_output_currency: float = 0.0
    total_accumulated_interest_in_output_currency: float = 0.0
    per_currency: dict[str, AccumulatorPerCurrency] = field(default_factory=dict)
