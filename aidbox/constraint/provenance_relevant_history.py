from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Provenance_Agent(BackboneElement):
	type: Optional[CodeableConcept] = None
	role: Optional[List[CodeableConcept]] = None
	who: Reference
	onBehalfOf: Optional[Reference] = None

class Provenance_Entity(BackboneElement):
	role: str
	what: Reference
	agent: Optional[List[str]] = None

class ProvenanceRelevantHistory(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/provenance-relevant-history"])
	signature: Optional[List[Signature]] = None
	occurredDateTime: Optional[str] = None
	recorded: str
	agent: List[Provenance_Agent]
	policy: Optional[List[str]] = None
	reason: Optional[List[CodeableConcept]] = None
	activity: CodeableConcept
	target: List[Reference]
	location: Optional[Reference] = None
	entity: Optional[List[Provenance_Entity]] = None