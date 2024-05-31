from pydantic import *
from typing import Optional, List
from ..base import *

class DocumentReference_Content(BackboneElement):
	attachment: Attachment
	format: Optional[Coding] = None

class DocumentReference_RelatesTo(BackboneElement):
	code: str
	target: Reference

class DocumentReference_Context(BackboneElement):
	encounter: Optional[List[Reference]] = None
	event: Optional[List[CodeableConcept]] = None
	period: Optional[Period] = None
	facilityType: Optional[CodeableConcept] = None
	practiceSetting: Optional[CodeableConcept] = None
	sourcePatientInfo: Optional[Reference] = None
	related: Optional[List[Reference]] = None

class DocumentReference(DomainResource):
	description: Optional[str] = None
	category: Optional[List[CodeableConcept]] = None
	date: Optional[str] = None
	docStatus: Optional[str] = None
	content: List[DocumentReference_Content]
	type: Optional[CodeableConcept] = None
	author: Optional[List[Reference]] = None
	masterIdentifier: Optional[Identifier] = None
	custodian: Optional[Reference] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	relatesTo: Optional[List[DocumentReference_RelatesTo]] = None
	context: Optional[DocumentReference_Context] = None
	securityLabel: Optional[List[CodeableConcept]] = None
	subject: Optional[Reference] = None
	authenticator: Optional[Reference] = None