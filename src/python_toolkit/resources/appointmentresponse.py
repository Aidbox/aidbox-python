from typing import Optional

from base import Reference
from base import Reference
from base import Identifier
from base import CodeableConcept
from base import DomainResource


class AppointmentResponse(DomainResource):
	actor: Optional[Reference] = None
	appointment: Reference
	comment: Optional[str] = None
	end: Optional[str] = None
	identifier: list[Identifier] = []
	participantStatus: str
	participantType: list[CodeableConcept] = []
	start: Optional[str] = None

