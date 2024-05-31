from pydantic import *
from typing import Optional, List
from ..base import *

class DeviceMetric_Calibration(BackboneElement):
	type: Optional[str] = None
	state: Optional[str] = None
	time: Optional[str] = None

class DeviceMetric(DomainResource):
	category: str
	measurementPeriod: Optional[Timing] = None
	color: Optional[str] = None
	parent: Optional[Reference] = None
	unit: Optional[CodeableConcept] = None
	type: CodeableConcept
	source: Optional[Reference] = None
	identifier: Optional[List[Identifier]] = None
	calibration: Optional[List[DeviceMetric_Calibration]] = None
	operationalStatus: Optional[str] = None