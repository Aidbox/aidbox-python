from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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

class UsCoreDocumentreference(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-documentreference"])
	description: Optional[str] = None
	category: List[CodeableConcept]
	date: Optional[str] = None
	docStatus: Optional[str] = None
	content: List[DocumentReference_Content]
	type: CodeableConcept
	author: Optional[List[Reference]] = None
	masterIdentifier: Optional[Identifier] = None
	custodian: Optional[Reference] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	relatesTo: Optional[List[DocumentReference_RelatesTo]] = None
	context: Optional[DocumentReference_Context] = None
	securityLabel: Optional[List[CodeableConcept]] = None
	subject: Reference
	authenticator: Optional[Reference] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None