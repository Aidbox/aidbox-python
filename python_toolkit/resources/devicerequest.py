from typing import Optional
from base import *

class DeviceRequest_Parameter(BackboneElement):
	code: Optional[CodeableConcept] = None
	valueBoolean: Optional[bool] = None
	valueCodeableConcept: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueRange: Optional[Range] = None

class DeviceRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	insurance: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	relevantHistory: list[Reference] = []
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	priorRequest: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	authoredOn: Optional[str] = None
	occurrenceTiming: Optional[str] = None
	note: list[Annotation] = []
	codeReference: Optional[Reference] = None
	requester: Optional[Reference] = None
	priority: Optional[str] = None
	occurrencePeriod: Optional[Period] = None
	status: Optional[str] = None
	codeCodeableConcept: Optional[CodeableConcept] = None
	groupIdentifier: Optional[Identifier] = None
	identifier: list[Identifier] = []
	intent: str
	basedOn: list[Reference] = []
	occurrenceDateTime: Optional[str] = None
	subject: Reference
	parameter: list[DeviceRequest_Parameter] = []
	performer: Optional[Reference] = None
	reasonReference: list[Reference] = []

