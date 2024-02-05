from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class Coding1217123003(Coding):
	display: Literal["Radiotherapy course of treatment (regime/therapy)"] = "Radiotherapy course of treatment (regime/therapy)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1217123003"] = "1217123003"

class CodexrtRadiotherapyCoursePrescriptionCode(CodeableConcept):
	coding: List[Coding1217123003] = [Coding1217123003()]


class CodexrtRadiotherapyCoursePrescription(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-course-prescription"])
	performerType: Optional[CodeableConcept] = None
	category: List[CodeableConcept]
	insurance: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	relevantHistory: Optional[List[Reference]] = None
	supportingInfo: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	patientInstruction: Optional[str] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[str] = None
	note: Optional[List[Annotation]] = None
	asNeededBoolean: Optional[bool] = None
	requisition: Optional[Identifier] = None
	locationReference: Optional[List[Reference]] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	quantityRatio: Optional[Ratio] = None
	code: CodexrtRadiotherapyCoursePrescriptionCode = CodexrtRadiotherapyCoursePrescriptionCode()
	identifier: Optional[List[Identifier]] = None
	bodySite: Optional[List[CodeableConcept]] = None
	intent: Literal["original-order"] = "original-order"
	quantityRange: Optional[Range] = None
	quantityQuantity: Optional[Quantity] = None
	replaces: Optional[List[Reference]] = None
	orderDetail: Optional[List[CodeableConcept]] = None
	basedOn: Optional[List[Reference]] = None
	locationCode: Optional[List[CodeableConcept]] = None
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	asNeededCodeableConcept: Optional[CodeableConcept] = None
	performer: Optional[List[Reference]] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None