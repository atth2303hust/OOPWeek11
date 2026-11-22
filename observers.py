# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Các lớp nhận thông báo cảnh báo (Observer)."""

from .contracts import IAlertObserver
from .events import Severity


class DashboardObserver(IAlertObserver):
    """Hiển thị thông báo lên màn hình."""

    def __init__(self, output=print):
        self.output = output

    def update(self, alert_event):
        text = (
            f"[DASHBOARD] {alert_event.sensor_name}: "
            f"{alert_event.value:.1f}{alert_event.unit} "
            f"[{alert_event.severity.value}]"
        )
        self.output(text)


class EmailAlertObserver(IAlertObserver):
    """Mô phỏng gửi email cảnh báo."""

    def __init__(self, recipient="safety@example.invalid", output=print):
        self.recipient = recipient
        self.output = output
        self.sent_messages = []

    def update(self, alert_event):
        message = (
            f"[EMAIL MO PHONG] To: {self.recipient} | "
            f"{alert_event.sensor_name} - {alert_event.severity.value} "
            f"({alert_event.value:.1f}{alert_event.unit})"
        )
        self.sent_messages.append(message)
        self.output(message)


class AuditLogObserver(IAlertObserver):
    """Lưu lịch sử các sự kiện cảnh báo."""

    def __init__(self, output=print):
        self.output = output
        self.events = []

    def update(self, alert_event):
        self.events.append(alert_event)
        text = (
            f"[AUDIT] {alert_event.occurred_at.isoformat()} | "
            f"{alert_event.severity.value} | {alert_event.sensor_name}"
        )
        self.output(text)


class EmergencyBridgeObserver(IAlertObserver):
    """Chuyển tiếp cảnh báo CRITICAL sang Mediator."""

    def __init__(self, mediator):
        if mediator is None:
            raise ValueError("Mediator không được None")
        self.mediator = mediator

    def update(self, alert_event):
        if alert_event.severity == Severity.CRITICAL:
            self.mediator.notify_emergency(alert_event)
