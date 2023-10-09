from typing import Optional
from base import *

class ImmunizationEvaluation(DomainResource):
	patient: Reference
	description: Optional[str] = None
	seriesDosesPositiveInt: Optional[str] = None
	date: Optional[str] = None
	doseNumberPositiveInt: Optional[str] = None
	series: Optional[str] = None
	authority: Optional[Reference] = None
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	doseStatusReason: list[CodeableConcept] = []
	immunizationEvent: Reference
	status: str
	identifier: list[Identifier] = []
	targetDisease: CodeableConcept
	doseStatus: CodeableConcept

