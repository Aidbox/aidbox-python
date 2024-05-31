from pydantic import *
from typing import Optional, List
from ..base import *

class Media(DomainResource):
	deviceName: Optional[str] = None
	encounter: Optional[Reference] = None
	content: Attachment
	frames: Optional[PositiveInt] = None
	width: Optional[PositiveInt] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	type: Optional[CodeableConcept] = None
	modality: Optional[CodeableConcept] = None
	duration: Optional[float] = None
	note: Optional[List[Annotation]] = None
	createdPeriod: Optional[Period] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	operator: Optional[Reference] = None
	bodySite: Optional[CodeableConcept] = None
	issued: Optional[str] = None
	device: Optional[Reference] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	createdDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	view: Optional[CodeableConcept] = None
	height: Optional[PositiveInt] = None