# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Các lớp cơ sở (interface) dùng chung."""


class ISensor:
    """Lớp cha cho các loại cảm biến."""

    def read_value(self):
        raise NotImplementedError("Cần cài đặt hàm read_value")

    def get_unit(self):
        raise NotImplementedError("Cần cài đặt hàm get_unit")


class IAlertObserver:
    """Lớp cha cho các đối tượng nhận cảnh báo."""

    def update(self, alert_event):
        raise NotImplementedError("Cần cài đặt hàm update")


class IEmergencyMediator:
    """Lớp cha cho bộ điều phối khẩn cấp."""

    def notify_emergency(self, alert_event):
        raise NotImplementedError("Cần cài đặt hàm notify_emergency")

    def reset(self):
        raise NotImplementedError("Cần cài đặt hàm reset")
