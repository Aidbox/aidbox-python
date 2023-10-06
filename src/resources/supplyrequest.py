from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Period
from base import Identifier
from base import CodeableConcept
from base import Quantity
from base import BackboneElement
from base import Reference
from base import DomainResource


class SupplyRequest(DomainResource):
	category: Optional[CodeableConcept] = None
	supplier: list[Reference] = []
	deliverTo: Optional[Reference] = None
	itemReference: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[str] = None
	deliverFrom: Optional[Reference] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	identifier: list[Identifier] = []
	itemCodeableConcept: Optional[CodeableConcept] = None
	quantity: Quantity
	occurrenceDateTime: Optional[str] = None
	parameter: list[BackboneElement] = []
	reasonReference: list[Reference] = []

