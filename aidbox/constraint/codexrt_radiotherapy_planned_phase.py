from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class Coding1222565005(Coding):
	display: Literal["Radiotherapy treatment phase (regime/therapy)"] = "Radiotherapy treatment phase (regime/therapy)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1222565005"] = "1222565005"

class CodexrtRadiotherapyPlannedPhaseCode(CodeableConcept):
	coding: List[Coding1222565005] = [Coding1222565005()]


class CodexrtRadiotherapyPlannedPhase(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-planned-phase"])
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
	code: CodexrtRadiotherapyPlannedPhaseCode = CodexrtRadiotherapyPlannedPhaseCode()
	identifier: Optional[List[Identifier]] = None
	bodySite: Optional[List[CodeableConcept]] = None
	intent: Literal["filler-order"] = "filler-order"
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
	extension: List[Extension]
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None