# /****************/
# MSSV: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Package Campus Safety Hub."""

from .adapter import SmokeSensorAdapter
from .contracts import IAlertObserver, IEmergencyMediator, ISensor
from .events import AlertEvent, Severity
from .legacy_sensor import LegacySmokeDetector
from .mediator import Alarm, DoorController, EmergencyMediator, VentilationController
from .monitor import SensorMonitor
from .observers import (
    AuditLogObserver,
    DashboardObserver,
    EmailAlertObserver,
    EmergencyBridgeObserver,
)
