from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding695486(Coding):
	system: Literal["http://loinc.org"] = "http://loinc.org"
	code: Literal["69548-6"] = "69548-6"

class McodeGenomicVariantCode(CodeableConcept):
	coding: List[Coding695486] = [Coding695486()]


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

class McodeGenomicVariant(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-genomic-variant"])
	category: List[CodeableConcept]
	referenceRange: Optional[List[Observation_ReferenceRange]] = None
	hasMember: Optional[List[Reference]] = None
	derivedFrom: Optional[List[Reference]] = None
	interpretation: Optional[List[CodeableConcept]] = None
	encounter: Optional[Reference] = None
	method: Optional[CodeableConcept] = None
	specimen: Optional[Reference] = None
	component: Optional[List[Observation_Component]] = None
	note: Optional[List[Annotation]] = None
	effectiveDateTime: Optional[str] = None
	status: str
	code: McodeGenomicVariantCode = McodeGenomicVariantCode()
	identifier: Optional[List[Identifier]] = None
	effectiveTiming: Optional[Timing] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	bodySite: Optional[CodeableConcept] = None
	focus: Optional[List[Reference]] = None
	issued: Optional[str] = None
	device: Optional[Reference] = None
	effectiveInstant: Optional[str] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	subject: Reference
	performer: Optional[List[Reference]] = None
	dataAbsentReason: Optional[CodeableConcept] = None
	effectivePeriod: Optional[Period] = None