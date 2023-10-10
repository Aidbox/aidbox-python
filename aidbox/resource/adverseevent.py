from typing import Optional
from ..base import *

class AdverseEvent_SuspectEntity_Causality(BackboneElement):
	assessment: Optional[CodeableConcept] = None
	author: Optional[Reference] = None
	method: Optional[CodeableConcept] = None
	productRelatedness: Optional[str] = None

class AdverseEvent_SuspectEntity(BackboneElement):
	causality: list[AdverseEvent_SuspectEntity_Causality] = []
	instance: Reference

class AdverseEvent(DomainResource):
	category: list[CodeableConcept] = []
	actuality: str
	date: Optional[str] = None
	study: list[Reference] = []
	encounter: Optional[Reference] = None
	suspectEntity: list[AdverseEvent_SuspectEntity] = []
	referenceDocument: list[Reference] = []
	outcome: Optional[CodeableConcept] = None
	recordedDate: Optional[str] = None
	event: Optional[CodeableConcept] = None
	contributor: list[Reference] = []
	subjectMedicalHistory: list[Reference] = []
	recorder: Optional[Reference] = None
	seriousness: Optional[CodeableConcept] = None
	severity: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	detected: Optional[str] = None
	location: Optional[Reference] = None
	subject: Reference
	resultingCondition: list[Reference] = []

