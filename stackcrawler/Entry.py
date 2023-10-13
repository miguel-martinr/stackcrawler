from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
  title: str
  order_number: int
  points: int