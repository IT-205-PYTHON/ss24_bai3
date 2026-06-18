"""
features/
Mỗi module tương ứng một chức năng trong menu.
Mỗi module đều export một hàm run() duy nhất.

Cách dùng trong main.py:
    from features import list_cards, register_card, ...
    list_cards.run(db)
"""

from features import (
    list_cards,
    register_card,
    earn_points,
    redeem_points,
    update_point_value,
)

__all__ = [
    "list_cards",
    "register_card",
    "earn_points",
    "redeem_points",
    "update_point_value",
]
