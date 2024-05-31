from pydantic import *
from typing import Optional, List
from ..base import *

class AdverseEvent_SuspectEntity_Causality(BackboneElement):
	assessment: Optional[CodeableConcept] = None
	productRelatedness: Optional[str] = None
	author: Optional[Reference] = None
	method: Optional[CodeableConcept] = None

class AdverseEvent_SuspectEntity(BackboneElement):
	instance: Reference
	causality: Optional[List[AdverseEvent_SuspectEntity_Causality]] = None

class AdverseEvent(DomainResource):
	category: Optional[List[CodeableConcept]] = None
	actuality: str
	date: Optional[str] = None
	study: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	suspectEntity: Optional[List[AdverseEvent_SuspectEntity]] = None
	referenceDocument: Optional[List[Reference]] = None
	outcome: Optional[CodeableConcept] = None
	recordedDate: Optional[str] = None
	event: Optional[CodeableConcept] = None
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