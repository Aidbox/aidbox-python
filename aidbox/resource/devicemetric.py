from typing import Optional
from ..base import *

class DeviceMetric_Calibration(BackboneElement):
	state: Optional[str] = None
	time: Optional[str] = None
	type: Optional[str] = None

class DeviceMetric(DomainResource):
	category: str
	measurementPeriod: Optional[str] = None
	color: Optional[str] = None
	parent: Optional[Reference] = None
	unit: Optional[CodeableConcept] = None
	type: CodeableConcept
	source: Optional[Reference] = None
	identifier: list[Identifier] = []
	calibration: list[DeviceMetric_Calibration] = []
	operationalStatus: Optional[str] = None

