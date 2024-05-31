from pydantic import *
from typing import Optional, List
from ..base import *

class SupplyDelivery_SuppliedItem(BackboneElement):
	quantity: Optional[Quantity] = None
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None

class SupplyDelivery(DomainResource):
	patient: Optional[Reference] = None
	supplier: Optional[Reference] = None
	suppliedItem: Optional[SupplyDelivery_SuppliedItem] = None
	type: Optional[CodeableConcept] = None
	occurrenceTiming: Optional[Timing] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	occurrenceDateTime: Optional[str] = None
	receiver: Optional[List[Reference]] = None
	destination: Optional[Reference] = None