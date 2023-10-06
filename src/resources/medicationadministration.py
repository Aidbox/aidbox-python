from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import Reference
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import BackboneElement
from base import Period
from base import Reference
from base import DomainResource


class MedicationAdministration(DomainResource):
	category: Optional[CodeableConcept] = None
	request: Optional[Reference] = None
	eventHistory: list[Reference] = []
	dosage: Optional[BackboneElement] = None
	instantiates: list[str] = []
	reasonCode: list[CodeableConcept] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: list[CodeableConcept] = []
	note: list[Annotation] = []
	supportingInformation: list[Reference] = []
	effectiveDateTime: Optional[str] = None
	status: str
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	device: list[Reference] = []
	medicationReference: Optional[Reference] = None
	partOf: list[Reference] = []
	subject: Reference
	performer: list[BackboneElement] = []
	effectivePeriod: Optional[Period] = None
	reasonReference: list[Reference] = []

