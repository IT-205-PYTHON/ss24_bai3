"""
features/register_card.py
Chức năng 2 — Đăng ký thẻ thành viên mới.
"""

from data import CardDatabase
from models import MemberCard
from utils import print_header, input_str


def run(db: CardDatabase) -> None:
    print_header("ĐĂNG KÝ THẺ THÀNH VIÊN MỚI")

    card_id = input_str("Nhập mã thẻ: ").upper()

    # Kiểm tra định dạng qua staticmethod — không cần tạo object
    if not MemberCard.is_valid_card_id(card_id):
        print(f"\nMã thẻ '{card_id}' không đúng định dạng!")
        print("Yêu cầu: bắt đầu bằng 'RC' + đúng 2 chữ số (VD: RC01, RC99).")
        return

    # Kiểm tra trùng mã
    if db.exists(card_id):
        print(f"\nMã thẻ '{card_id}' đã tồn tại trong hệ thống!")
        print("Vui lòng kiểm tra lại.")
        return

    name = input_str("Nhập tên khách hàng: ")
    if not name:
        print("\nTên khách hàng không được để trống!")
        return

    card = MemberCard(card_id, name)
    db.add(card)

    print(f"\nĐăng ký thẻ thành viên thành công!")
    print(f"  Mã thẻ       : {card.card_id}")
    print(f"  Tên khách    : {card.name}")
    print(f"  Điểm ban đầu : {card.points}")
    print(f"  Hạng thẻ     : {card.tier}")
