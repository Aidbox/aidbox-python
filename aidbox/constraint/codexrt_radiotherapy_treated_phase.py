from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding108290001(Coding):
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["108290001"] = "108290001"

class CodexrtRadiotherapyTreatedPhaseCategory(CodeableConcept):
	coding: List[Coding108290001] = [Coding108290001()]

class Coding1222565005(Coding):
	display: Literal["Radiotherapy treatment phase (regime/therapy)"] = "Radiotherapy treatment phase (regime/therapy)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1222565005"] = "1222565005"

class CodexrtRadiotherapyTreatedPhaseCode(CodeableConcept):
	coding: List[Coding1222565005] = [Coding1222565005()]


class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference
	onBehalfOf: Optional[Reference] = None

class CodexrtRadiotherapyTreatedPhase(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-treated-phase"])
	category: Optional[CodexrtRadiotherapyTreatedPhaseCategory] = None
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
	code: CodexrtRadiotherapyTreatedPhaseCode = CodexrtRadiotherapyTreatedPhaseCode()
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