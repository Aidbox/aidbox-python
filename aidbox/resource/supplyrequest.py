from pydantic import *
from typing import Optional, List
from ..base import *

class SupplyRequest_Parameter(BackboneElement):
	code: Optional[CodeableConcept] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueRange: Optional[Range] = None
	valueBoolean: Optional[bool] = None

class SupplyRequest(DomainResource):
	category: Optional[CodeableConcept] = None
	supplier: Optional[List[Reference]] = None
	deliverTo: Optional[Reference] = None
	itemReference: Optional[Reference] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[Timing] = None
	deliverFrom: Optional[Reference] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	itemCodeableConcept: Optional[CodeableConcept] = None
	quantity: Quantity
	occurrenceDateTime: Optional[str] = None
	parameter: Optional[List[SupplyRequest_Parameter]] = None
	reasonReference: Optional[List[Reference]] = None