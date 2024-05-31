from pydantic import *
from typing import Optional, List
from ..base import *

class ChargeItem_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference

class ChargeItem(DomainResource):
	service: Optional[List[Reference]] = None
	definitionUri: Optional[List[str]] = None
	enterer: Optional[Reference] = None
	requestingOrganization: Optional[Reference] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	productReference: Optional[Reference] = None
	definitionCanonical: Optional[List[str]] = None
	bodysite: Optional[List[CodeableConcept]] = None
	occurrenceTiming: Optional[Timing] = None
	costCenter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	account: Optional[List[Reference]] = None
	reason: Optional[List[CodeableConcept]] = None
	supportingInformation: Optional[List[Reference]] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	code: CodeableConcept
	identifier: Optional[List[Identifier]] = None
	context: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	partOf: Optional[List[Reference]] = None
	priceOverride: Optional[Money] = None
	enteredDate: Optional[str] = None
	occurrenceDateTime: Optional[str] = None
	overrideReason: Optional[str] = None
	performingOrganization: Optional[Reference] = None
	subject: Reference
	factorOverride: Optional[float] = None
	performer: Optional[List[ChargeItem_Performer]] = None