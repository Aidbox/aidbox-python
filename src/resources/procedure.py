from typing import Optional

from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Annotation
from base import Range
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Period
from base import Reference
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import DomainResource


class Procedure(DomainResource):
	category: Optional[CodeableConcept] = None
	report: list[Reference] = []
	usedCode: list[CodeableConcept] = []
	usedReference: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	focalDevice: list[BackboneElement] = []
	encounter: Optional[Reference] = None
	performedAge: Optional[str] = None
	complicationDetail: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	performedString: Optional[str] = None
	statusReason: Optional[CodeableConcept] = None
	outcome: Optional[CodeableConcept] = None
	asserter: Optional[Reference] = None
	note: list[Annotation] = []
	performedRange: Optional[Range] = None
	complication: list[CodeableConcept] = []
	status: str
	performedDateTime: Optional[str] = None
	recorder: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	bodySite: list[CodeableConcept] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	performedPeriod: Optional[Period] = None
	location: Optional[Reference] = None
	followUp: list[CodeableConcept] = []
	subject: Reference
	performer: list[BackboneElement] = []
	reasonReference: list[Reference] = []

