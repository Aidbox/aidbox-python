from pydantic import *
from typing import Optional, List
from ..base import *

class AppointmentResponse(DomainResource):
	identifier: Optional[List[Identifier]] = None
	appointment: Reference
	start: Optional[str] = None
	end: Optional[str] = None
	participantType: Optional[List[CodeableConcept]] = None
	actor: Optional[Reference] = None
	participantStatus: str
	comment: Optional[str] = None