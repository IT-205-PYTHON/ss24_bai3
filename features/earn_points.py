"""
features/earn_points.py
Chức năng 3 — Khách mua hàng / tích điểm.
"""

from data import CardDatabase
from utils import print_header, input_str, input_float, format_vnd


def run(db: CardDatabase) -> None:
    print_header("KHÁCH MUA HÀNG - TÍCH ĐIỂM")

    card_id = input_str("Nhập mã thẻ: ")
    card = db.find_by_id(card_id)
    if not card:
        print(f"\nKhông tìm thấy thẻ '{card_id.upper()}' trong hệ thống!")
        return

    bill_amount = input_float("Nhập tổng tiền hóa đơn: ")
    if bill_amount is None or bill_amount <= 0:
        print("\nSố tiền hóa đơn không hợp lệ!")
        return

    result = card.earn_points(bill_amount)

    print(f"\n  Khách hàng    : {result['name']}")
    print(f"  Hóa đơn       : {format_vnd(result['bill_amount'])}")
    print(f"  Điểm được tích: {result['earned']}")
    print(f"  Tổng điểm     : {result['total']}")

    if result["upgraded"]:
        print(f"\n  🎉 Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")

    print(f"  Hạng thẻ      : {result['tier']}")
