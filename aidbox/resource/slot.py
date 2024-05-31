from pydantic import *
from typing import Optional, List
from ..base import *

class Slot(DomainResource):
	schedule: Reference
	serviceCategory: Optional[List[CodeableConcept]] = None
	specialty: Optional[List[CodeableConcept]] = None
	start: str
	serviceType: Optional[List[CodeableConcept]] = None
	appointmentType: Optional[CodeableConcept] = None
	status: str
	comment: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	end: str
	overbooked: Optional[bool] = None