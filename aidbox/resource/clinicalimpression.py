from pydantic import *
from typing import Optional, List
from ..base import *

class ClinicalImpression_Investigation(BackboneElement):
	code: CodeableConcept
	item: Optional[List[Reference]] = None

class ClinicalImpression_Finding(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	basis: Optional[str] = None

class ClinicalImpression(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	investigation: Optional[List[ClinicalImpression_Investigation]] = None
	protocol: Optional[List[str]] = None
	assessor: Optional[Reference] = None
	supportingInfo: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	problem: Optional[List[Reference]] = None
	statusReason: Optional[CodeableConcept] = None
	note: Optional[List[Annotation]] = None
	summary: Optional[str] = None
	effectiveDateTime: Optional[str] = None
	prognosisCodeableConcept: Optional[List[CodeableConcept]] = None
	status: str
	previous: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	finding: Optional[List[ClinicalImpression_Finding]] = None
	prognosisReference: Optional[List[Reference]] = None
	subject: Reference
	effectivePeriod: Optional[Period] = None