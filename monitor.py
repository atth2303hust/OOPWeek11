# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Bộ giám sát cảm biến và gửi thông báo tới các observer."""

from datetime import datetime, timezone

from .events import AlertEvent, Severity


class SensorMonitor:
    """Kiểm tra chỉ số cảm biến, phân loại mức độ và báo cho observer."""

    def __init__(self, now=None):
        self.observers = []
        self.now = now
        self.notification_errors = []

    def _get_current_time(self):
        if self.now is not None:
            return self.now()
        return datetime.now(timezone.utc)

    def attach(self, observer):
        if observer is None:
            raise ValueError("Observer không được None")
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def check_sensor(self, sensor_name, sensor):
        if not sensor_name or not sensor_name.strip():
            raise ValueError("Tên cảm biến không hợp lệ")
        if sensor is None:
            raise ValueError("Sensor không được None")

        value = sensor.read_value()
        if value < 0 or value > 100:
            raise ValueError(f"Giá trị cảm biến ngoài miền 0..100: {value}")

        if value >= 70:
            severity = Severity.CRITICAL
        elif value >= 50:
            severity = Severity.WARNING
        else:
            return None

        event = AlertEvent(
            sensor_name=sensor_name,
            value=value,
            unit=sensor.get_unit(),
            severity=severity,
            occurred_at=self._get_current_time(),
        )
        self._notify(event)
        return event

    def _notify(self, event):
        # Duyệt trên bản copy để tránh lỗi nếu observer tự hủy đăng ký
        for observer in list(self.observers):
            try:
                observer.update(event)
            except Exception as err:
                detail = f"{type(observer).__name__}: {type(err).__name__}: {err}"
                self.notification_errors.append(detail)
                print("Cảnh báo lỗi observer:", detail)
