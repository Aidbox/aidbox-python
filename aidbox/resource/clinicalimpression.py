from typing import Optional
from ..base import *

class ClinicalImpression_Investigation(BackboneElement):
	code: CodeableConcept
	item: list[Reference] = []

class ClinicalImpression_Finding(BackboneElement):
	basis: Optional[str] = None
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None

class ClinicalImpression(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	investigation: list[ClinicalImpression_Investigation] = []
	protocol: list[str] = []
	assessor: Optional[Reference] = None
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	problem: list[Reference] = []
	statusReason: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	summary: Optional[str] = None
	effectiveDateTime: Optional[str] = None
	prognosisCodeableConcept: list[CodeableConcept] = []
	status: str
	previous: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	finding: list[ClinicalImpression_Finding] = []
	prognosisReference: list[Reference] = []
	subject: Reference
	effectivePeriod: Optional[Period] = None

