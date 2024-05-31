from pydantic import *
from typing import Optional, List
from ..base import *

class ImmunizationEvaluation(DomainResource):
	patient: Reference
	description: Optional[str] = None
	seriesDosesPositiveInt: Optional[PositiveInt] = None
	date: Optional[str] = None
	doseNumberPositiveInt: Optional[PositiveInt] = None
	series: Optional[str] = None
	authority: Optional[Reference] = None
	doseNumberString: Optional[str] = None
	seriesDosesString: Optional[str] = None
	doseStatusReason: Optional[List[CodeableConcept]] = None
	immunizationEvent: Reference
	status: str
	identifier: Optional[List[Identifier]] = None
	targetDisease: CodeableConcept
	doseStatus: CodeableConcept