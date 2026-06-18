"""
features/list_cards.py
Chức năng 1 — Xem danh sách thẻ thành viên.
"""

from data import CardDatabase
from utils import print_header, print_divider


def run(db: CardDatabase) -> None:
    print_header("DANH SÁCH THẺ THÀNH VIÊN")
    cards = db.all()

    if not cards:
        print("Chưa có thẻ nào trong hệ thống.")
        return

    print_divider()
    for i, card in enumerate(cards, 1):
        print(card.as_list_row(i))
    print_divider()
    print(f"Tổng số thẻ: {len(cards)}")
