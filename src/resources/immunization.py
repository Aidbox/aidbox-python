from typing import Optional

from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Quantity
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import Annotation
from base import Identifier
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import DomainResource


class Immunization(DomainResource):
	patient: Reference
	isSubpotent: Optional[bool] = None
	reportOrigin: Optional[CodeableConcept] = None
	protocolApplied: list[BackboneElement] = []
	site: Optional[CodeableConcept] = None
	encounter: Optional[Reference] = None
	vaccineCode: CodeableConcept
	doseQuantity: Optional[Quantity] = None
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	route: Optional[CodeableConcept] = None
	recorded: Optional[str] = None
	programEligibility: list[CodeableConcept] = []
	note: list[Annotation] = []
	primarySource: Optional[bool] = None
	status: str
	lotNumber: Optional[str] = None
	identifier: list[Identifier] = []
	manufacturer: Optional[Reference] = None
	education: list[BackboneElement] = []
	occurrenceString: Optional[str] = None
	reaction: list[BackboneElement] = []
	location: Optional[Reference] = None
	occurrenceDateTime: Optional[str] = None
	fundingSource: Optional[CodeableConcept] = None
	subpotentReason: list[CodeableConcept] = []
	expirationDate: Optional[str] = None
	performer: list[BackboneElement] = []
	reasonReference: list[Reference] = []

