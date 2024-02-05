from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class Coding108290001(Coding):
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["108290001"] = "108290001"

class McodeRadiotherapyCourseSummaryCategory(CodeableConcept):
	coding: List[Coding108290001] = [Coding108290001()]

class Coding1217123003(Coding):
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1217123003"] = "1217123003"

class McodeRadiotherapyCourseSummaryCode(CodeableConcept):
	coding: List[Coding1217123003] = [Coding1217123003()]


class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference
	onBehalfOf: Optional[Reference] = None

class McodeRadiotherapyCourseSummary(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-radiotherapy-course-summary"])
	category: McodeRadiotherapyCourseSummaryCategory = McodeRadiotherapyCourseSummaryCategory()
	report: Optional[List[Reference]] = None
	usedCode: Optional[List[CodeableConcept]] = None
	usedReference: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	focalDevice: Optional[List[Procedure_FocalDevice]] = None
	encounter: Optional[Reference] = None
	complicationDetail: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	statusReason: Optional[CodeableConcept] = None
	outcome: Optional[CodeableConcept] = None
	asserter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	complication: Optional[List[CodeableConcept]] = None
	status: str
	recorder: Optional[Reference] = None
	code: McodeRadiotherapyCourseSummaryCode = McodeRadiotherapyCourseSummaryCode()
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