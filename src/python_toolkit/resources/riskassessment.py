from typing import Optional

from base import Reference
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Annotation
from base import Period
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class RiskAssessment(DomainResource):
	parent: Optional[Reference] = None
	encounter: Optional[Reference] = None
	prediction: list[BackboneElement] = []
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

