from typing import Optional
from ..base import *

class Observation_ReferenceRange(BackboneElement):
	age: Optional[Range] = None
	appliesTo: list[CodeableConcept] = []
	high: Optional[Quantity] = None
	low: Optional[Quantity] = None
	text: Optional[str] = None
	type: Optional[CodeableConcept] = None

class Observation_Component(BackboneElement):
	referenceRange: list[str] = []
	interpretation: list[CodeableConcept] = []
	valueTime: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueRatio: Optional[Ratio] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueSampledData: Optional[SampledData] = None
	code: CodeableConcept
	valueCodeableConcept: Optional[CodeableConcept] = None
	valuePeriod: Optional[Period] = None
	valueRange: Optional[Range] = None
	valueInteger: Optional[int] = None
	dataAbsentReason: Optional[CodeableConcept] = None

class Observation(DomainResource):
	category: list[CodeableConcept] = []
	referenceRange: list[Observation_ReferenceRange] = []
	hasMember: list[Reference] = []
	derivedFrom: list[Reference] = []
	interpretation: list[CodeableConcept] = []
	encounter: Optional[Reference] = None
	method: Optional[CodeableConcept] = None
	valueTime: Optional[str] = None
	specimen: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueRatio: Optional[Ratio] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	component: list[Observation_Component] = []
	note: list[Annotation] = []
	valueSampledData: Optional[SampledData] = None
	effectiveDateTime: Optional[str] = None
	status: str
	code: CodeableConcept
	identifier: list[Identifier] = []
	effectiveTiming: Optional[str] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	bodySite: Optional[CodeableConcept] = None
	focus: list[Reference] = []
	issued: Optional[str] = None
	valuePeriod: Optional[Period] = None
	device: Optional[Reference] = None
	effectiveInstant: Optional[str] = None
	basedOn: list[Reference] = []
	valueRange: Optional[Range] = None
	partOf: list[Reference] = []
	valueInteger: Optional[int] = None
	subject: Optional[Reference] = None
	performer: list[Reference] = []
	dataAbsentReason: Optional[CodeableConcept] = None
	effectivePeriod: Optional[Period] = None

