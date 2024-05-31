from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class AdverseEvent_SuspectEntity_Causality(BackboneElement):
	assessment: Optional[CodeableConcept] = None
	productRelatedness: Optional[str] = None
	author: Optional[Reference] = None
	method: Optional[CodeableConcept] = None

class AdverseEvent_SuspectEntity(BackboneElement):
	instance: Reference
	causality: Optional[List[AdverseEvent_SuspectEntity_Causality]] = None

class CodexrtRadiotherapyAdverseEvent(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-adverse-event"])
	category: Optional[List[CodeableConcept]] = None
	actuality: Literal["actual"] = "actual"
	date: Optional[str] = None
	study: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	suspectEntity: Optional[List[AdverseEvent_SuspectEntity]] = None
	referenceDocument: Optional[List[Reference]] = None
	outcome: Optional[CodeableConcept] = None
	recordedDate: Optional[str] = None
	event: CodeableConcept
	contributor: Optional[List[Reference]] = None
	subjectMedicalHistory: Optional[List[Reference]] = None
	recorder: Optional[Reference] = None
	seriousness: Optional[CodeableConcept] = None
	severity: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	detected: Optional[str] = None
	location: Optional[Reference] = None
	subject: Reference
	resultingCondition: Optional[List[Reference]] = None