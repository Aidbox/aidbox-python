from typing import Optional
from ..base import *

class RiskAssessment_Prediction(BackboneElement):
	relativeRisk: Optional[str] = None
	whenRange: Optional[Range] = None
	outcome: Optional[CodeableConcept] = None
	whenPeriod: Optional[Period] = None
	rationale: Optional[str] = None
	probabilityRange: Optional[Range] = None
	qualitativeRisk: Optional[CodeableConcept] = None
	probabilityDecimal: Optional[str] = None

class RiskAssessment(DomainResource):
	parent: Optional[Reference] = None
	encounter: Optional[Reference] = None
	prediction: list[RiskAssessment_Prediction] = []
	method: Optional[CodeableConcept] = None
	basis: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	mitigation: Optional[str] = None
	note: list[Annotation] = []
	occurrencePeriod: Optional[Period] = None
	status: str
	condition: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	basedOn: Optional[Reference] = None
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	performer: Optional[Reference] = None
	reasonReference: list[Reference] = []

