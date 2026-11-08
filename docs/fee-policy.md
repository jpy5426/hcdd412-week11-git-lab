# Late Fee Policy

The campus library desk charges late fees according to these rules:

- Fees accrue per calendar day an item is late, at the item's daily rate.
- Items returned on time or early are never charged.
- **Grace period:** the first `grace_days` days late are free; fees are charged only for days beyond the grace period (default: 0).
- **Maximum fee:** a fee never exceeds the item's maximum fee (`max_fee`), when one is set. The grace period is applied first, then the maximum fee.
