# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Mediator điều phối còi, cửa và hệ thống hút khói."""

from .contracts import IEmergencyMediator
from .events import Severity


class Alarm:
    """Còi báo động."""

    def __init__(self):
        self.active = False
        self.history = []

    def activate(self):
        self.active = True
        self.history.append("Bật còi cảnh báo")

    def deactivate(self):
        self.active = False
        self.history.append("Tắt còi cảnh báo")


class DoorController:
    """Bộ điều khiển cửa thoát hiểm."""

    def __init__(self):
        self.locked = True
        self.history = []

    def unlock(self):
        self.locked = False
        self.history.append("Mở khóa cửa thoát hiểm")

    def lock(self):
        self.locked = True
        self.history.append("Khóa lại cửa")


class VentilationController:
    """Bộ điều khiển quạt hút khói."""

    def __init__(self):
        self.extracting = False
        self.history = []

    def start_extraction(self):
        self.extracting = True
        self.history.append("Bật thông gió hút khói")

    def stop_extraction(self):
        self.extracting = False
        self.history.append("Tắt thông gió hút khói")


class EmergencyMediator(IEmergencyMediator):
    """Điều phối trung tâm khi có sự cố khẩn cấp."""

    def __init__(self, alarm, door, ventilation):
        self.alarm = alarm
        self.door = door
        self.ventilation = ventilation
        self.handled_events = []

    def notify_emergency(self, alert_event):
        if alert_event.severity != Severity.CRITICAL:
            return
        self.alarm.activate()
        self.door.unlock()
        self.ventilation.start_extraction()
        self.handled_events.append(alert_event)

    def reset(self):
        self.alarm.deactivate()
        self.door.lock()
        self.ventilation.stop_extraction()
