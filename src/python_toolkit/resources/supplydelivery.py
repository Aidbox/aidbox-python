from typing import Optional
from base import *

class SupplyDelivery_SuppliedItem(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	quantity: Optional[Quantity] = None

class SupplyDelivery(DomainResource):
	patient: Optional[Reference] = None
	supplier: Optional[Reference] = None
	suppliedItem: Optional[SupplyDelivery_SuppliedItem] = None
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

