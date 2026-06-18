from models.member_card import MemberCard


class CardDatabase:
    """
    Lớp quản lý tập hợp các MemberCard trong bộ nhớ.
    Đóng vai trò Repository — tách biệt logic lưu trữ khỏi nghiệp vụ.
    """

    def __init__(self) -> None:
        self._cards: list[MemberCard] = []

    # ── Truy vấn ─────────────────────────────────────────────

    def all(self) -> list[MemberCard]:
        return list(self._cards)

    def find_by_id(self, card_id: str) -> MemberCard | None:
        target = card_id.upper()
        for card in self._cards:
            if card.card_id == target:
                return card
        return None

    def exists(self, card_id: str) -> bool:
        return self.find_by_id(card_id) is not None

    # ── Ghi ──────────────────────────────────────────────────

    def add(self, card: MemberCard) -> None:
        self._cards.append(card)

    # ── Seed dữ liệu mẫu ─────────────────────────────────────

    def seed(self) -> None:
        """Khởi tạo dữ liệu mẫu để demo."""
        sample = [
            ("RC01", "Nguyen Van A", 150, MemberCard.TIER_VIP),
            ("RC02", "Tran Thi B",   20,  MemberCard.TIER_STANDARD),
        ]
        for card_id, name, points, tier in sample:
            card = MemberCard(card_id, name)
            # Gán trực tiếp qua mangled name — chỉ dùng nội bộ khi seed
            card._MemberCard__points = points
            card._MemberCard__tier   = tier
            self._cards.append(card)
