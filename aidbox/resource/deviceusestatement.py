from pydantic import *
from typing import Optional, List
from ..base import *

class DeviceUseStatement(DomainResource):
	derivedFrom: Optional[List[Reference]] = None
	timingPeriod: Optional[Period] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	source: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[Timing] = None
	status: str
	recordedOn: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	bodySite: Optional[CodeableConcept] = None
	device: Reference
	basedOn: Optional[List[Reference]] = None
	subject: Reference
	reasonReference: Optional[List[Reference]] = None