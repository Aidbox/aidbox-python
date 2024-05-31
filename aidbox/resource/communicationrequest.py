from pydantic import *
from typing import Optional, List
from ..base import *

class CommunicationRequest_Payload(BackboneElement):
	contentString: Optional[str] = None
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class CommunicationRequest(DomainResource):
	category: Optional[List[CodeableConcept]] = None
	payload: Optional[List[CommunicationRequest_Payload]] = None
	encounter: Optional[Reference] = None
	medium: Optional[List[CodeableConcept]] = None
	recipient: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	note: Optional[List[Annotation]] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	sender: Optional[Reference] = None
	identifier: Optional[List[Identifier]] = None
	doNotPerform: Optional[bool] = None
	replaces: Optional[List[Reference]] = None
	basedOn: Optional[List[Reference]] = None
	occurrenceDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	about: Optional[List[Reference]] = None
	reasonReference: Optional[List[Reference]] = None