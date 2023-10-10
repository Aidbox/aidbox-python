from typing import Optional
from ..base import *

class Slot(DomainResource):
	schedule: Reference
	serviceCategory: list[CodeableConcept] = []
	specialty: list[CodeableConcept] = []
	start: str
	serviceType: list[CodeableConcept] = []
	appointmentType: Optional[CodeableConcept] = None
	status: str
	comment: Optional[str] = None
	identifier: list[Identifier] = []
	end: str
	overbooked: Optional[bool] = None

