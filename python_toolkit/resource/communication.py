from typing import Optional
from ..base import *

class Communication_Payload(BackboneElement):
	contentAttachment: Optional[Attachment] = None
	contentReference: Optional[Reference] = None
	contentString: Optional[str] = None

class Communication(DomainResource):
	category: list[CodeableConcept] = []
	received: Optional[str] = None
	instantiatesCanonical: list[str] = []
	payload: list[Communication_Payload] = []
	instantiatesUri: list[str] = []
	encounter: Optional[Reference] = None
	medium: list[CodeableConcept] = []
	recipient: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	topic: Optional[CodeableConcept] = None
	sent: Optional[str] = None
	note: list[Annotation] = []
	priority: Optional[str] = None
	status: str
	sender: Optional[Reference] = None
	identifier: list[Identifier] = []
	inResponseTo: list[Reference] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	subject: Optional[Reference] = None
	about: list[Reference] = []
	reasonReference: list[Reference] = []

