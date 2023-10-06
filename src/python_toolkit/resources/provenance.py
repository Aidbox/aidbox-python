from typing import Optional

from base import Signature
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import BackboneElement
from base import Period
from base import DomainResource


class Provenance(DomainResource):
	signature: list[Signature] = []
	occurredDateTime: Optional[str] = None
	recorded: str
	agent: list[BackboneElement]
	policy: list[str] = []
	reason: list[CodeableConcept] = []
	activity: Optional[CodeableConcept] = None
	target: list[Reference]
	location: Optional[Reference] = None
	entity: list[BackboneElement] = []
	occurredPeriod: Optional[Period] = None

