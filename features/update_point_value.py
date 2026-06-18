"""
features/update_point_value.py
Chức năng 5 — Cập nhật tỷ giá quy đổi điểm (dành cho quản lý hệ thống).
"""

from models import MemberCard
from utils import print_header, input_int, format_vnd


def run() -> None:
    print_header("CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM")
    print(f"  Tỷ giá hiện tại: 1 điểm = {format_vnd(MemberCard.point_value_vnd)}")

    new_value = input_int("Nhập tỷ giá mới cho 1 điểm (VNĐ): ")
    if new_value is None or new_value <= 0:
        print("\nTỷ giá không hợp lệ! Vui lòng nhập số nguyên dương.")
        return

    MemberCard.update_point_value(new_value)
    print(f"\nCập nhật tỷ giá thành công!")
    print(f"  Tỷ giá mới: 1 điểm = {format_vnd(MemberCard.point_value_vnd)}")
