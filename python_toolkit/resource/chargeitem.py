from typing import Optional
from ..base import *

class ChargeItem_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None

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
	performer: list[ChargeItem_Performer] = []

