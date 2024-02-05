from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference
	onBehalfOf: Optional[Reference] = None

class UsCoreProcedure(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"])
	category: Optional[CodeableConcept] = None
	report: Optional[List[Reference]] = None
	usedCode: Optional[List[CodeableConcept]] = None
	usedReference: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	focalDevice: Optional[List[Procedure_FocalDevice]] = None
	encounter: Optional[Reference] = None
	performedAge: Optional[str] = None
	complicationDetail: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	performedString: Optional[str] = None
	statusReason: Optional[CodeableConcept] = None
	outcome: Optional[CodeableConcept] = None
	asserter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	performedRange: Optional[Range] = None
	complication: Optional[List[CodeableConcept]] = None
	status: str
	performedDateTime: Optional[str] = None
	recorder: Optional[Reference] = None
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	bodySite: Optional[List[CodeableConcept]] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	performedPeriod: Optional[Period] = None
	location: Optional[Reference] = None
	followUp: Optional[List[CodeableConcept]] = None
	subject: Reference
	performer: Optional[List[Procedure_Performer]] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None