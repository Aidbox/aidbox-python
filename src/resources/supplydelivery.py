from typing import Optional

from base import Reference
from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class SupplyDelivery(DomainResource):
	patient: Optional[Reference] = None
	supplier: Optional[Reference] = None
	suppliedItem: Optional[BackboneElement] = None
	type: Optional[CodeableConcept] = None
	occurrenceTiming: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	identifier: list[Identifier] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	occurrenceDateTime: Optional[str] = None
	receiver: list[Reference] = []
	destination: Optional[Reference] = None

