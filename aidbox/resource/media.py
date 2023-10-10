from typing import Optional
from ..base import *

class Media(DomainResource):
	deviceName: Optional[str] = None
	encounter: Optional[Reference] = None
	content: Attachment
	frames: Optional[str] = None
	width: Optional[str] = None
	reasonCode: list[CodeableConcept] = []
	type: Optional[CodeableConcept] = None
	modality: Optional[CodeableConcept] = None
	duration: Optional[str] = None
	note: list[Annotation] = []
	createdPeriod: Optional[Period] = None
	status: str
	identifier: list[Identifier] = []
	operator: Optional[Reference] = None
	bodySite: Optional[CodeableConcept] = None
	issued: Optional[str] = None
	device: Optional[Reference] = None
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	createdDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	view: Optional[CodeableConcept] = None
	height: Optional[str] = None

