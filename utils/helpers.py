"""
utils/helpers.py
Các hàm tiện ích dùng chung: nhập liệu có kiểm tra, format hiển thị.
"""


def input_int(prompt: str) -> int | None:
    """Nhận số nguyên từ người dùng. Trả về None nếu không hợp lệ."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        return None


def input_float(prompt: str) -> float | None:
    """Nhận số thực từ người dùng. Trả về None nếu không hợp lệ."""
    try:
        return float(input(prompt).strip())
    except ValueError:
        return None


def input_str(prompt: str) -> str:
    """Nhận chuỗi không rỗng từ người dùng."""
    return input(prompt).strip()


def print_divider(char: str = "─", width: int = 52) -> None:
    print(char * width)


def print_header(title: str) -> None:
    print(f"\n--- {title} ---")


def format_vnd(amount: int | float) -> str:
    return f"{amount:,.0f} VNĐ"
