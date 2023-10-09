from typing import Optional
from ..base import *

class DocumentReference_Content(BackboneElement):
	attachment: Attachment
	format: Optional[Coding] = None

class DocumentReference_RelatesTo(BackboneElement):
	code: str
	target: Reference

class DocumentReference_Context(BackboneElement):
	encounter: list[Reference] = []
	event: list[CodeableConcept] = []
	facilityType: Optional[CodeableConcept] = None
	period: Optional[Period] = None
	practiceSetting: Optional[CodeableConcept] = None
	related: list[Reference] = []
	sourcePatientInfo: Optional[Reference] = None

class DocumentReference(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	date: Optional[str] = None
	docStatus: Optional[str] = None
	content: list[DocumentReference_Content]
	type: Optional[CodeableConcept] = None
	author: list[Reference] = []
	masterIdentifier: Optional[Identifier] = None
	custodian: Optional[Reference] = None
	status: str
	identifier: list[Identifier] = []
	relatesTo: list[DocumentReference_RelatesTo] = []
	context: Optional[DocumentReference_Context] = None
	securityLabel: list[CodeableConcept] = []
	subject: Optional[Reference] = None
	authenticator: Optional[Reference] = None

