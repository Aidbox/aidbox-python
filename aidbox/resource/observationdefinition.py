from pydantic import *
from typing import Optional, List
from ..base import *

class ObservationDefinition_QuantitativeDetails(BackboneElement):
	customaryUnit: Optional[CodeableConcept] = None
	unit: Optional[CodeableConcept] = None
	conversionFactor: Optional[float] = None
	decimalPrecision: Optional[int] = None

class ObservationDefinition_QualifiedInterval(BackboneElement):
	category: Optional[str] = None
	range: Optional[Range] = None
	context: Optional[CodeableConcept] = None
	appliesTo: Optional[List[CodeableConcept]] = None
	gender: Optional[str] = None
	age: Optional[Range] = None
	gestationalAge: Optional[Range] = None
	condition: Optional[str] = None

class ObservationDefinition(DomainResource):
	quantitativeDetails: Optional[ObservationDefinition_QuantitativeDetails] = None
	category: Optional[List[CodeableConcept]] = None
	method: Optional[CodeableConcept] = None
	validCodedValueSet: Optional[Reference] = None
	qualifiedInterval: Optional[List[ObservationDefinition_QualifiedInterval]] = None
	abnormalCodedValueSet: Optional[Reference] = None
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	permittedDataType: Optional[List[str]] = None
	multipleResultsAllowed: Optional[bool] = None
	normalCodedValueSet: Optional[Reference] = None
	preferredReportName: Optional[str] = None
	criticalCodedValueSet: Optional[Reference] = None