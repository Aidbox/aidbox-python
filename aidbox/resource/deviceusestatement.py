from typing import Optional
from ..base import *

class DeviceUseStatement(DomainResource):
	derivedFrom: list[Reference] = []
	timingPeriod: Optional[Period] = None
	reasonCode: list[CodeableConcept] = []
	source: Optional[Reference] = None
	note: list[Annotation] = []
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	status: str
	recordedOn: Optional[str] = None
	identifier: list[Identifier] = []
	bodySite: Optional[CodeableConcept] = None
	device: Reference
	basedOn: list[Reference] = []
	subject: Reference
	reasonReference: list[Reference] = []

