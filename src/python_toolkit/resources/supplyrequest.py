from typing import Optional
from base import *

class SupplyRequest_Parameter(BackboneElement):
	code: Optional[CodeableConcept] = None
	valueBoolean: Optional[bool] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueRange: Optional[Range] = None

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
	parameter: list[SupplyRequest_Parameter] = []
	reasonReference: list[Reference] = []

