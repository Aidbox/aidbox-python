from pydantic import *
from typing import Optional, List
from ..base import *

class RiskAssessment_Prediction(BackboneElement):
	relativeRisk: Optional[float] = None
	whenRange: Optional[Range] = None
	outcome: Optional[CodeableConcept] = None
	whenPeriod: Optional[Period] = None
	rationale: Optional[str] = None
	probabilityRange: Optional[Range] = None
	qualitativeRisk: Optional[CodeableConcept] = None
	probabilityDecimal: Optional[float] = None

class RiskAssessment(DomainResource):
	parent: Optional[Reference] = None
	encounter: Optional[Reference] = None
	prediction: Optional[List[RiskAssessment_Prediction]] = None
	method: Optional[CodeableConcept] = None
	basis: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	mitigation: Optional[str] = None
	note: Optional[List[Annotation]] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	condition: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	basedOn: Optional[Reference] = None
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	performer: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None