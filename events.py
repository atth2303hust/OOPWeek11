# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Lưu trữ thông tin sự kiện cảnh báo."""

from enum import Enum


class Severity(Enum):
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class AlertEvent:
    """Đối tượng chứa thông tin một lần cảnh báo."""

    def __init__(self, sensor_name, value, unit, severity, occurred_at):
        if not sensor_name or not sensor_name.strip():
            raise ValueError("Tên cảm biến không được để trống")
        if occurred_at.tzinfo is None:
            raise ValueError("Thời điểm phải kèm múi giờ")

        self.sensor_name = sensor_name
        self.value = value
        self.unit = unit
        self.severity = severity
        self.occurred_at = occurred_at
