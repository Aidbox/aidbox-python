from typing import Optional

from base import Coding
from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import BackboneElement
from base import Coding
from base import DomainResource


class AuditEvent(DomainResource):
	outcomeDesc: Optional[str] = None
	type: Coding
	outcome: Optional[str] = None
	source: BackboneElement
	recorded: str
	agent: list[BackboneElement]
	purposeOfEvent: list[CodeableConcept] = []
	action: Optional[str] = None
	period: Optional[Period] = None
	entity: list[BackboneElement] = []
	subtype: list[Coding] = []

