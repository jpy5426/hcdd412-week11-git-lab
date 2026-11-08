"""Late-fee calculation for the campus library desk."""

from typing import Optional


def late_fee(
    days_late: int,
    daily_rate: float,
    grace_days: int = 0,
    max_fee: Optional[float] = None,
) -> float:
    """Return the late fee in dollars for an item returned ``days_late`` days late.

    Items returned on time or early are never charged. The first ``grace_days``
    days late are free; only the days beyond the grace period are charged.
    When ``max_fee`` is given, the fee never exceeds it. The grace period is
    applied first, then the cap.
    """
    chargeable_days = days_late - grace_days
    if chargeable_days <= 0:
        return 0.0
    fee = round(chargeable_days * daily_rate, 2)
    if max_fee is not None:
        fee = min(fee, max_fee)
    return fee