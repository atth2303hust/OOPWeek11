# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Chạy thử chương trình Campus Safety Hub."""

import sys
from datetime import datetime, timezone

from campus_safety_hub import (
    Alarm,
    AuditLogObserver,
    DashboardObserver,
    DoorController,
    EmailAlertObserver,
    EmergencyBridgeObserver,
    EmergencyMediator,
    LegacySmokeDetector,
    SensorMonitor,
    SmokeSensorAdapter,
    VentilationController,
)


def fixed_time():
    return datetime(2026, 11, 22, 3, 0, tzinfo=timezone.utc)


def run_demo(levels):
    legacy = LegacySmokeDetector(0)
    sensor = SmokeSensorAdapter(legacy)

    alarm = Alarm()
    door = DoorController()
    ventilation = VentilationController()
    mediator = EmergencyMediator(alarm, door, ventilation)

    monitor = SensorMonitor(now=fixed_time)

    dashboard = DashboardObserver()
    email = EmailAlertObserver()
    audit = AuditLogObserver()
    bridge = EmergencyBridgeObserver(mediator)

    monitor.attach(dashboard)
    monitor.attach(email)
    monitor.attach(audit)
    monitor.attach(bridge)
    monitor.attach(dashboard)  # Đăng ký trùng sẽ bị bỏ qua

    print("=== CAMPUS SAFETY HUB - LAB W11 ===")
    print(f"So observer ban dau: {len(monitor.observers)} (mong doi 4)")

    index = 1
    for raw in levels:
        legacy.set_smoke_level(raw)
        print(f"\n[Mau {index}] Muc khoi cu: {legacy.get_smoke_level()}/1000 -> {sensor.read_value():.1f}{sensor.get_unit()}")

        event = monitor.check_sensor("Phong may A1", sensor)
        if event is None:
            print("[MONITOR] NORMAL: khong phat canh bao")
        elif event.severity.value == "CRITICAL":
            print("[MEDIATOR] Coi=BAT, Cua=MO, Hut khoi=BAT")

        if index == 2:
            monitor.detach(email)
            print("[OBSERVER] Da huy dang ky EmailAlertObserver")

        index += 1

    print("\n=== TRANG THAI CUOI ===")
    print("Alarm active:", alarm.active)
    print("Door unlocked:", not door.locked)
    print("Ventilation extracting:", ventilation.extracting)
    print("Audit events:", len(audit.events))
    print("Emergency events:", len(mediator.handled_events))
    print("Notification errors:", len(monitor.notification_errors))

    mediator.reset()
    print(
        f"Sau reset: alarm={alarm.active}, door_locked={door.locked}, "
        f"ventilation={ventilation.extracting}"
    )


if __name__ == "__main__":
    # Đọc tham số --levels đơn giản nếu người dùng truyền vào từ terminal
    levels = [350, 500, 699, 700, 735, 490]
    if "--levels" in sys.argv:
        pos = sys.argv.index("--levels")
        levels = [int(x) for x in sys.argv[pos + 1:]]

    run_demo(levels)
