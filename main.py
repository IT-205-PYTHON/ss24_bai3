"""

Entry point của ứng dụng Rikkei Coffee Member Card System.

"""

from data import CardDatabase
from features import (
    list_cards,
    register_card,
    earn_points,
    redeem_points,
    update_point_value,
)

MENU = """
╔══════════════════════════════════════════════════════╗
║      HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE           ║
╠══════════════════════════════════════════════════════╣
║  1. Xem danh sách thẻ thành viên                     ║
║  2. Đăng ký thẻ mới                                  ║
║  3. Khách mua hàng (Tích điểm)                       ║
║  4. Khách dùng điểm (Đổi ưu đãi)                     ║
║  5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)          ║
║  6. Thoát chương trình                               ║
╚══════════════════════════════════════════════════════╝"""

HANDLERS = {
    "1": lambda db: list_cards.run(db),
    "2": lambda db: register_card.run(db),
    "3": lambda db: earn_points.run(db),
    "4": lambda db: redeem_points.run(db),
    "5": lambda db: update_point_value.run(),
}


def main() -> None:
    db = CardDatabase()
    db.seed()  # Tải dữ liệu mẫu

    while True:
        print(MENU)
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        handler = HANDLERS.get(choice)
        if handler:
            handler(db)
        else:
            print("\nChức năng không hợp lệ! Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()
