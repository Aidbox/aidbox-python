from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import CodeableConcept
from base import Reference
from base import Quantity
from base import Identifier
from base import Reference
from base import Reference
from base import Quantity
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import BackboneElement
from base import DomainResource


class MedicationDispense(DomainResource):
	statusReasonReference: Optional[Reference] = None
	category: Optional[CodeableConcept] = None
	whenHandedOver: Optional[str] = None
	whenPrepared: Optional[str] = None
	eventHistory: list[Reference] = []
	substitution: Optional[BackboneElement] = None
	detectedIssue: list[Reference] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	statusReasonCodeableConcept: Optional[CodeableConcept] = None
	supportingInformation: list[Reference] = []
	status: str
	dosageInstruction: list[str] = []
	daysSupply: Optional[Quantity] = None
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	partOf: list[Reference] = []
	location: Optional[Reference] = None
	authorizingPrescription: list[Reference] = []
	receiver: list[Reference] = []
	subject: Optional[Reference] = None
	destination: Optional[Reference] = None
	performer: list[BackboneElement] = []

