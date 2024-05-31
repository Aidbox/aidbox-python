from pydantic import *
from typing import Optional, List
from ..base import *

class ServiceRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	category: Optional[List[CodeableConcept]] = None
	insurance: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	relevantHistory: Optional[List[Reference]] = None
	supportingInfo: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	patientInstruction: Optional[str] = None
	specimen: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[Timing] = None
	note: Optional[List[Annotation]] = None
	asNeededBoolean: Optional[bool] = None
	requisition: Optional[Identifier] = None
	locationReference: Optional[List[Reference]] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: str
	quantityRatio: Optional[Ratio] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	doNotPerform: Optional[bool] = None
	bodySite: Optional[List[CodeableConcept]] = None
	intent: str
	quantityRange: Optional[Range] = None
	quantityQuantity: Optional[Quantity] = None
	replaces: Optional[List[Reference]] = None
	orderDetail: Optional[List[CodeableConcept]] = None
	basedOn: Optional[List[Reference]] = None
	locationCode: Optional[List[CodeableConcept]] = None
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	asNeededCodeableConcept: Optional[CodeableConcept] = None
	performer: Optional[List[Reference]] = None
	reasonReference: Optional[List[Reference]] = None