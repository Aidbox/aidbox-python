from typing import Optional
from base import *

class AppointmentResponse(DomainResource):
	actor: Optional[Reference] = None
	appointment: Reference
	comment: Optional[str] = None
	end: Optional[str] = None
	identifier: list[Identifier] = []
	participantStatus: str
	participantType: list[CodeableConcept] = []
	start: Optional[str] = None

