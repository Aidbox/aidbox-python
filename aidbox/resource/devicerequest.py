from pydantic import *
from typing import Optional, List
from ..base import *

class DeviceRequest_Parameter(BackboneElement):
	code: Optional[CodeableConcept] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueRange: Optional[Range] = None
	valueBoolean: Optional[bool] = None

class DeviceRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	insurance: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	relevantHistory: Optional[List[Reference]] = None
	supportingInfo: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	priorRequest: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[Timing] = None
	note: Optional[List[Annotation]] = None
	codeReference: Optional[Reference] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	codeCodeableConcept: Optional[CodeableConcept] = None
	groupIdentifier: Optional[Identifier] = None
	identifier: Optional[List[Identifier]] = None
	intent: str
	basedOn: Optional[List[Reference]] = None
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	parameter: Optional[List[DeviceRequest_Parameter]] = None
	performer: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None