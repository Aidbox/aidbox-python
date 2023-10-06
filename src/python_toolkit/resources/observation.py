from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Quantity
from base import Ratio
from base import BackboneElement
from base import Annotation
from base import SampledData
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Period
from base import Reference
from base import Reference
from base import Range
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Period
from base import DomainResource


class Observation(DomainResource):
	category: list[CodeableConcept] = []
	referenceRange: list[BackboneElement] = []
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
	component: list[BackboneElement] = []
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

