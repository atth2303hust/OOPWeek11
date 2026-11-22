# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Mô phỏng cảm biến khói đời cũ (không sửa đổi)."""


class LegacySmokeDetector:
    """Cảm biến cũ trả về mức khói từ 0 đến 1000."""

    def __init__(self, smoke_level):
        self._smoke_level = smoke_level

    def get_smoke_level(self):
        return self._smoke_level

    def get_description(self):
        return "Legacy smoke detector"

    def set_smoke_level(self, value):
        if value < 0:
            self._smoke_level = 0
        elif value > 1000:
            self._smoke_level = 1000
        else:
            self._smoke_level = value
