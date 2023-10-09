from typing import Optional
from ..base import *

class CommunicationRequest_Payload(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None
	contentString: Optional[str] = None

class CommunicationRequest(DomainResource):
	category: list[CodeableConcept] = []
	payload: list[CommunicationRequest_Payload] = []
	encounter: Optional[Reference] = None
	medium: list[CodeableConcept] = []
	recipient: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	note: list[Annotation] = []
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	sender: Optional[Reference] = None
	identifier: list[Identifier] = []
	doNotPerform: Optional[bool] = None
	replaces: list[Reference] = []
	basedOn: list[Reference] = []
	occurrenceDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	about: list[Reference] = []
	reasonReference: list[Reference] = []

