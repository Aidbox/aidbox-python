from typing import Optional
from base import *

class ObservationDefinition_QuantitativeDetails(BackboneElement):
	conversionFactor: Optional[str] = None
	customaryUnit: Optional[CodeableConcept] = None
	decimalPrecision: Optional[int] = None
	unit: Optional[CodeableConcept] = None

class ObservationDefinition_QualifiedInterval(BackboneElement):
	age: Optional[Range] = None
	appliesTo: list[CodeableConcept] = []
	category: Optional[str] = None
	condition: Optional[str] = None
	context: Optional[CodeableConcept] = None
	gender: Optional[str] = None
	gestationalAge: Optional[Range] = None
	range: Optional[Range] = None

class ObservationDefinition(DomainResource):
	quantitativeDetails: Optional[ObservationDefinition_QuantitativeDetails] = None
	category: list[CodeableConcept] = []
	method: Optional[CodeableConcept] = None
	validCodedValueSet: Optional[Reference] = None
	qualifiedInterval: list[ObservationDefinition_QualifiedInterval] = []
	abnormalCodedValueSet: Optional[Reference] = None
	code: CodeableConcept
	identifier: list[Identifier] = []
	permittedDataType: list[str] = []
	multipleResultsAllowed: Optional[bool] = None
	normalCodedValueSet: Optional[Reference] = None
	preferredReportName: Optional[str] = None
	criticalCodedValueSet: Optional[Reference] = None

