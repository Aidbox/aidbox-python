from pydantic import *
from typing import Optional, List
from ..base import *

class AuditEvent_Source(BackboneElement):
	site: Optional[str] = None
	observer: Reference
	type: Optional[List[Coding]] = None

class AuditEvent_Agent_Network(BackboneElement):
	address: Optional[str] = None
	type: Optional[str] = None

class AuditEvent_Agent(BackboneElement):
	role: Optional[List[CodeableConcept]] = None
	requestor: bool
	who: Optional[Reference] = None
	altId: Optional[str] = None
	name: Optional[str] = None
	type: Optional[CodeableConcept] = None
	policy: Optional[List[str]] = None
	purposeOfUse: Optional[List[CodeableConcept]] = None
	network: Optional[AuditEvent_Agent_Network] = None
	location: Optional[Reference] = None
	media: Optional[Coding] = None

class AuditEvent_Entity_Detail(BackboneElement):
	type: str
	valueString: Optional[str] = None
	valueBase64Binary: Optional[str] = None

class AuditEvent_Entity(BackboneElement):
	role: Optional[Coding] = None
	description: Optional[str] = None
	name: Optional[str] = None
	type: Optional[Coding] = None
	lifecycle: Optional[Coding] = None
	query: Optional[str] = None
	securityLabel: Optional[List[Coding]] = None
	what: Optional[Reference] = None
	detail: Optional[List[AuditEvent_Entity_Detail]] = None

class AuditEvent(DomainResource):
	outcomeDesc: Optional[str] = None
	type: Coding
	outcome: Optional[str] = None
	source: AuditEvent_Source
	recorded: str
	agent: List[AuditEvent_Agent]
	purposeOfEvent: Optional[List[CodeableConcept]] = None
	action: Optional[str] = None
	period: Optional[Period] = None
	entity: Optional[List[AuditEvent_Entity]] = None
	subtype: Optional[List[Coding]] = None