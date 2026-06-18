# Rikkei Coffee — Member Card System

Hệ thống quản lý thẻ thành viên chạy trên Terminal, xây dựng theo chuẩn OOP.

## Cách chạy

```bash
cd rikkei_coffee
python main.py
```

## Cấu trúc dự án

```
rikkei_coffee/
│
├── main.py                         # Entry point — menu loop
│
├── models/
│   └── member_card.py              # Class MemberCard (OOP core)
│
├── data/
│   └── database.py                 # CardDatabase — quản lý danh sách thẻ
│
├── features/                       # Mỗi chức năng = 1 module độc lập
│   ├── list_cards.py               # CF1: Xem danh sách
│   ├── register_card.py            # CF2: Đăng ký thẻ mới
│   ├── earn_points.py              # CF3: Tích điểm
│   ├── redeem_points.py            # CF4: Đổi điểm
│   └── update_point_value.py       # CF5: Cập nhật tỷ giá
│
└── utils/
    └── helpers.py                  # Hàm tiện ích dùng chung (I/O, format)
```

## Nguyên tắc thiết kế

| Thành phần | Trách nhiệm |
|---|---|
| `models/` | Định nghĩa cấu trúc dữ liệu và logic nghiệp vụ thuần tuý |
| `data/` | Lưu trữ và truy vấn tập hợp objects (Repository pattern) |
| `features/` | Mỗi chức năng là một module: nhận input → gọi model → in output |
| `utils/` | Helpers dùng chung, không phụ thuộc domain |
| `main.py` | Điều phối luồng chính, không chứa logic nghiệp vụ |

## OOP Decorators sử dụng

- `@property` — đọc `points` và `tier` một cách an toàn (không có setter công khai)
- `@staticmethod` — `is_valid_card_id`: kiểm tra định dạng mã thẻ, không cần object
- `@classmethod` — `update_point_value`: cập nhật tỷ giá đồng bộ toàn hệ thống
- Name Mangling (`__points`, `__tier`) — ngăn gán trực tiếp từ bên ngoài class
