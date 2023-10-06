from typing import Optional

from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Annotation
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Period
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Quantity
from base import Reference
from base import Money
from base import Reference
from base import Reference
from base import BackboneElement
from base import DomainResource


class ChargeItem(DomainResource):
	service: list[Reference] = []
	definitionUri: list[str] = []
	enterer: Optional[Reference] = None
	requestingOrganization: Optional[Reference] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	productReference: Optional[Reference] = None
	definitionCanonical: list[str] = []
	bodysite: list[CodeableConcept] = []
	occurrenceTiming: Optional[str] = None
	costCenter: Optional[Reference] = None
	note: list[Annotation] = []
	account: list[Reference] = []
	reason: list[CodeableConcept] = []
	supportingInformation: list[Reference] = []
	occurrencePeriod: Optional[Period] = None
	status: str
	code: CodeableConcept
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	partOf: list[Reference] = []
	priceOverride: Optional[Money] = None
	enteredDate: Optional[str] = None
	occurrenceDateTime: Optional[str] = None
	overrideReason: Optional[str] = None
	performingOrganization: Optional[Reference] = None
	subject: Reference
	factorOverride: Optional[str] = None
	performer: list[BackboneElement] = []

