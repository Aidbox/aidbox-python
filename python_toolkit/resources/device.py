from typing import Optional
from base import *

class Device_DeviceName(BackboneElement):
	name: str
	type: str

class Device_Property(BackboneElement):
	type: CodeableConcept
	valueCode: list[CodeableConcept] = []
	valueQuantity: list[Quantity] = []

class Device_Specialization(BackboneElement):
	systemType: CodeableConcept
	version: Optional[str] = None

class Device_Version(BackboneElement):
	component: Optional[Identifier] = None
	type: Optional[CodeableConcept] = None
	value: str

class Device_UdiCarrier(BackboneElement):
	carrierAIDC: Optional[str] = None
	carrierHRF: Optional[str] = None
	deviceIdentifier: Optional[str] = None
	entryType: Optional[str] = None
	issuer: Optional[str] = None
	jurisdiction: Optional[str] = None

class Device(DomainResource):
	patient: Optional[Reference] = None
	definition: Optional[Reference] = None
	serialNumber: Optional[str] = None
	parent: Optional[Reference] = None
	deviceName: list[Device_DeviceName] = []
	property: list[Device_Property] = []
	partNumber: Optional[str] = None
	modelNumber: Optional[str] = None
	type: Optional[CodeableConcept] = None
	statusReason: list[CodeableConcept] = []
	specialization: list[Device_Specialization] = []
	distinctIdentifier: Optional[str] = None
	note: list[Annotation] = []
	status: Optional[str] = None
	safety: list[CodeableConcept] = []
	lotNumber: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	manufacturer: Optional[str] = None
	version: list[Device_Version] = []
	location: Optional[Reference] = None
	contact: list[ContactPoint] = []
	manufactureDate: Optional[str] = None
	owner: Optional[Reference] = None
	expirationDate: Optional[str] = None
	udiCarrier: list[Device_UdiCarrier] = []

