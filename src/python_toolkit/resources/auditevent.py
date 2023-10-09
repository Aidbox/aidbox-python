from typing import Optional
from base import *

class AuditEvent_Source(BackboneElement):
	observer: Reference
	site: Optional[str] = None
	type: list[Coding] = []

class AuditEvent_Agent_Network(BackboneElement):
	address: Optional[str] = None
	type: Optional[str] = None

class AuditEvent_Agent(BackboneElement):
	role: list[CodeableConcept] = []
	requestor: bool
	who: Optional[Reference] = None
	altId: Optional[str] = None
	name: Optional[str] = None
	type: Optional[CodeableConcept] = None
	policy: list[str] = []
	purposeOfUse: list[CodeableConcept] = []
	network: Optional[AuditEvent_Agent_Network] = None
	location: Optional[Reference] = None
	media: Optional[Coding] = None

class AuditEvent_Entity_Detail(BackboneElement):
	type: str
	valueBase64Binary: Optional[str] = None
	valueString: Optional[str] = None

class AuditEvent_Entity(BackboneElement):
	role: Optional[Coding] = None
	description: Optional[str] = None
	name: Optional[str] = None
	type: Optional[Coding] = None
	lifecycle: Optional[Coding] = None
	query: Optional[str] = None
	securityLabel: list[Coding] = []
	what: Optional[Reference] = None
	detail: list[AuditEvent_Entity_Detail] = []

class AuditEvent(DomainResource):
	outcomeDesc: Optional[str] = None
	type: Coding
	outcome: Optional[str] = None
	source: AuditEvent_Source
	recorded: str
	agent: list[AuditEvent_Agent]
	purposeOfEvent: list[CodeableConcept] = []
	action: Optional[str] = None
	period: Optional[Period] = None
	entity: list[AuditEvent_Entity] = []
	subtype: list[Coding] = []

