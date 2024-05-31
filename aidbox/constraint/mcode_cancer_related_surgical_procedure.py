from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding387713003(Coding):
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["387713003"] = "387713003"

class McodeCancerRelatedSurgicalProcedureCategory(CodeableConcept):
	coding: List[Coding387713003] = [Coding387713003()]


class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference
	onBehalfOf: Optional[Reference] = None

class McodeCancerRelatedSurgicalProcedure(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-cancer-related-surgical-procedure"])
	category: McodeCancerRelatedSurgicalProcedureCategory = McodeCancerRelatedSurgicalProcedureCategory()
	report: Optional[List[Reference]] = None
	usedCode: Optional[List[CodeableConcept]] = None
	usedReference: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	focalDevice: Optional[List[Procedure_FocalDevice]] = None
	encounter: Optional[Reference] = None
	performedAge: Optional[Age] = None
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