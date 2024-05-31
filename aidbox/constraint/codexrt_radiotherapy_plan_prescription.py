from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding1255724003(Coding):
	display: Literal["Radiotherapy treatment plan (regime/therapy)"] = "Radiotherapy treatment plan (regime/therapy)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1255724003"] = "1255724003"

class CodexrtRadiotherapyPlanPrescriptionCode(CodeableConcept):
	coding: List[Coding1255724003] = [Coding1255724003()]


class CodexrtRadiotherapyPlanPrescription(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-plan-prescription"])
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
	occurrenceTiming: Optional[Timing] = None
	note: Optional[List[Annotation]] = None
	asNeededBoolean: Optional[bool] = None
	requisition: Optional[Identifier] = None
	locationReference: Optional[List[Reference]] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	quantityRatio: Optional[Ratio] = None
	code: CodexrtRadiotherapyPlanPrescriptionCode = CodexrtRadiotherapyPlanPrescriptionCode()
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