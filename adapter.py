# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Adapter chuyển đổi giá trị từ cảm biến cũ sang thang đo mới."""

from .contracts import ISensor


class SmokeSensorAdapter(ISensor):
    """Chuyển mức khói 0..1000 về phần trăm 0..100."""

    def __init__(self, legacy):
        if legacy is None:
            raise ValueError("LegacySmokeDetector không được None")
        self.legacy = legacy

    def read_value(self):
        return self.legacy.get_smoke_level() / 10.0

    def get_unit(self):
        return "% smoke"
