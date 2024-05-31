from pydantic import *
from typing import Optional, List
from ..base import *

class Communication_Payload(BackboneElement):
	contentString: Optional[str] = None
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None

class Communication(DomainResource):
	category: Optional[List[CodeableConcept]] = None
	received: Optional[str] = None
	instantiatesCanonical: Optional[List[str]] = None
	payload: Optional[List[Communication_Payload]] = None
	instantiatesUri: Optional[List[str]] = None
	encounter: Optional[Reference] = None
	medium: Optional[List[CodeableConcept]] = None
	recipient: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	statusReason: Optional[CodeableConcept] = None
	topic: Optional[CodeableConcept] = None
	sent: Optional[str] = None
	note: Optional[List[Annotation]] = None
	priority: Optional[str] = None
	status: str
	sender: Optional[Reference] = None
	identifier: Optional[List[Identifier]] = None
	inResponseTo: Optional[List[Reference]] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	subject: Optional[Reference] = None
	about: Optional[List[Reference]] = None
	reasonReference: Optional[List[Reference]] = None