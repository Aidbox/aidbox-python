from typing import Optional
from ..base import *

class Provenance_Agent(BackboneElement):
	onBehalfOf: Optional[Reference] = None
	role: list[CodeableConcept] = []
	type: Optional[CodeableConcept] = None
	who: Reference

class Provenance_Entity(BackboneElement):
	agent: list[str] = []
	role: str
	what: Reference

class Provenance(DomainResource):
	signature: list[Signature] = []
	occurredDateTime: Optional[str] = None
	recorded: str
	agent: list[Provenance_Agent]
	policy: list[str] = []
	reason: list[CodeableConcept] = []
	activity: Optional[CodeableConcept] = None
	target: list[Reference]
	location: Optional[Reference] = None
	entity: list[Provenance_Entity] = []
	occurredPeriod: Optional[Period] = None

