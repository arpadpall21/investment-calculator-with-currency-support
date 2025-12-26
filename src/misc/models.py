from dataclasses import dataclass, field


@dataclass
class Accumulator:
    capital: float = 0.0
    interest: float = 0.0


@dataclass
class Bank:
    per_currency: dict[str, Accumulator] = field(default_factory=dict)
    total_in_output_currency: Accumulator = field(default_factory=Accumulator)
