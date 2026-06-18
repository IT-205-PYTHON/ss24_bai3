"""
features/redeem_points.py
Chức năng 4 — Khách dùng điểm / đổi ưu đãi.
"""

from data import CardDatabase
from models import MemberCard
from utils import print_header, input_str, input_int, format_vnd


def run(db: CardDatabase) -> None:
    print_header("KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI")
    print(f"  (Tỷ giá hiện tại: 1 điểm = {format_vnd(MemberCard.point_value_vnd)})")

    card_id = input_str("Nhập mã thẻ: ")
    card = db.find_by_id(card_id)
    if not card:
        print(f"\nKhông tìm thấy thẻ '{card_id.upper()}' trong hệ thống!")
        return

    points_to_use = input_int("Nhập số điểm muốn sử dụng: ")
    if points_to_use is None:
        print("\nSố điểm không hợp lệ! Vui lòng nhập số nguyên.")
        return

    result = card.redeem_points(points_to_use)

    if not result["success"]:
        print(f"\nKhông thể đổi điểm!")
        print(f"Số điểm muốn sử dụng vượt quá số điểm hiện có.")
        print(f"  Điểm hiện tại       : {result['current_points']}")
        print(f"  Số điểm sau giao dịch: {result['current_points']} (giữ nguyên)")
        return

    print(f"\n  Đã trừ {result['points_used']} điểm.")
    print(f"  Khách hàng được giảm giá {format_vnd(result['discount'])} vào hóa đơn!")
    print(f"  Số điểm còn lại : {result['remaining']}")
    print(f"  Hạng thẻ        : {result['tier']}")
