from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Observation_ReferenceRange(BackboneElement):
	low: Optional[Quantity] = None
	high: Optional[Quantity] = None
	type: Optional[CodeableConcept] = None
	appliesTo: Optional[List[CodeableConcept]] = None
	age: Optional[Range] = None
	text: Optional[str] = None

class Observation_Component(BackboneElement):
	referenceRange: Optional[List[str]] = None
	interpretation: Optional[List[CodeableConcept]] = None
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

class Heartrate(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/heartrate"])
	category: List[CodeableConcept]
	referenceRange: Optional[List[Observation_ReferenceRange]] = None
	hasMember: Optional[List[Reference]] = None
	derivedFrom: Optional[List[Reference]] = None
	interpretation: Optional[List[CodeableConcept]] = None
	encounter: Optional[Reference] = None
	method: Optional[CodeableConcept] = None
	valueTime: Optional[str] = None
	specimen: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueRatio: Optional[Ratio] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	component: Optional[List[Observation_Component]] = None
	note: Optional[List[Annotation]] = None
	valueSampledData: Optional[SampledData] = None
	effectiveDateTime: Optional[str] = None
	status: str
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	bodySite: Optional[CodeableConcept] = None
	focus: Optional[List[Reference]] = None
	issued: Optional[str] = None
	valuePeriod: Optional[Period] = None
	device: Optional[Reference] = None
	basedOn: Optional[List[Reference]] = None
	valueRange: Optional[Range] = None
	partOf: Optional[List[Reference]] = None
	valueInteger: Optional[int] = None
	subject: Reference
	performer: Optional[List[Reference]] = None
	dataAbsentReason: Optional[CodeableConcept] = None
	effectivePeriod: Optional[Period] = None