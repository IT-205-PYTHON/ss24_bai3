import re


class MemberCard:
    """
    Model đại diện cho một thẻ thành viên Rikkei Coffee.

    Class Attribute:
        point_value_vnd (int): Giá trị quy đổi chung toàn hệ thống (VNĐ/điểm).

    Instance Attributes:
        card_id  (str): Mã thẻ (định dạng RC + 2 chữ số).
        name     (str): Tên khách hàng (title-case).
        __points (int): Điểm tích lũy — private, chỉ thay đổi qua nghiệp vụ.
        __tier   (str): Hạng thẻ — private, tự động cập nhật.
    """

    point_value_vnd: int = 1000

    TIER_STANDARD = "Standard"
    TIER_VIP      = "VIP"
    VIP_THRESHOLD = 100

    def __init__(self, card_id: str, name: str) -> None:
        self.card_id = card_id.upper()
        self.name    = name.title()
        self.__points: int = 0
        self.__tier: str   = self.TIER_STANDARD

    # ── Getters ──────────────────────────────────────────────

    @property
    def points(self) -> int:
        return self.__points

    @property
    def tier(self) -> str:
        return self.__tier

    # ── Static Method: validation ────────────────────────────

    @staticmethod
    def is_valid_card_id(card_id: str) -> bool:
        """Trả về True khi card_id khớp định dạng RC + đúng 2 chữ số."""
        return bool(re.fullmatch(r"RC\d{2}", card_id))

    # ── Class Method: cập nhật tỷ giá toàn hệ thống ─────────

    @classmethod
    def update_point_value(cls, new_value: int) -> None:
        """Thay đổi point_value_vnd cho tất cả thẻ."""
        cls.point_value_vnd = new_value

    # ── Instance Methods: nghiệp vụ ──────────────────────────

    def earn_points(self, bill_amount: float) -> dict:
        """
        Tích điểm từ hóa đơn (10,000 VNĐ = 1 điểm).
        Trả về dict chứa kết quả để feature layer hiển thị.
        """
        earned = int(bill_amount // 10_000)
        self.__points += earned

        upgraded = False
        if self.__points >= self.VIP_THRESHOLD and self.__tier != self.TIER_VIP:
            self.__tier = self.TIER_VIP
            upgraded = True

        return {
            "name":        self.name,
            "bill_amount": bill_amount,
            "earned":      earned,
            "total":       self.__points,
            "tier":        self.__tier,
            "upgraded":    upgraded,
        }

    def redeem_points(self, points_to_use: int) -> dict:
        """
        Đổi điểm lấy ưu đãi.
        Trả về dict success/failure để feature layer hiển thị.
        """
        if points_to_use <= 0 or points_to_use > self.__points:
            return {
                "success":       False,
                "current_points": self.__points,
            }

        self.__points -= points_to_use

        if self.__points < self.VIP_THRESHOLD and self.__tier == self.TIER_VIP:
            self.__tier = self.TIER_STANDARD

        discount = points_to_use * MemberCard.point_value_vnd
        return {
            "success":        True,
            "points_used":    points_to_use,
            "discount":       discount,
            "remaining":      self.__points,
            "tier":           self.__tier,
        }

    # ── Hiển thị dòng danh sách ──────────────────────────────

    def as_list_row(self, index: int) -> str:
        return (
            f"{index}. Mã: {self.card_id:<5} | "
            f"Tên: {self.name:<20} | "
            f"Điểm: {self.__points:<5} | "
            f"Hạng: {self.__tier}"
        )
