from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class AdverseEvent(DomainResource):
	category: list[CodeableConcept] = []
	actuality: str
	date: Optional[str] = None
	study: list[Reference] = []
	encounter: Optional[Reference] = None
	suspectEntity: list[BackboneElement] = []
	referenceDocument: list[Reference] = []
	outcome: Optional[CodeableConcept] = None
	recordedDate: Optional[str] = None
	event: Optional[CodeableConcept] = None
	contributor: list[Reference] = []
	subjectMedicalHistory: list[Reference] = []
	recorder: Optional[Reference] = None
	seriousness: Optional[CodeableConcept] = None
	severity: Optional[CodeableConcept] = None
	identifier: Optional[Identifier] = None
	detected: Optional[str] = None
	location: Optional[Reference] = None
	subject: Reference
	resultingCondition: list[Reference] = []

