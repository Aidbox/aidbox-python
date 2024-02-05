from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Device_DeviceName(BackboneElement):
	name: str
	type: str

class Device_Property(BackboneElement):
	type: CodeableConcept
	valueQuantity: Optional[List[Quantity]] = None
	valueCode: Optional[List[CodeableConcept]] = None

class Device_Specialization(BackboneElement):
	systemType: CodeableConcept
	version: Optional[str] = None

class Device_Version(BackboneElement):
	type: Optional[CodeableConcept] = None
	component: Optional[Identifier] = None
	value: str

class Device_UdiCarrier(BackboneElement):
	deviceIdentifier: Optional[str] = None
	issuer: Optional[str] = None
	jurisdiction: Optional[str] = None
	carrierAIDC: Optional[str] = None
	carrierHRF: Optional[str] = None
	entryType: Optional[str] = None

class CodexrtRadiotherapySeedDevice(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-seed-device"])
	patient: Reference
	definition: Optional[Reference] = None
	serialNumber: Optional[str] = None
	parent: Optional[Reference] = None
	deviceName: Optional[List[Device_DeviceName]] = None
	property: Optional[List[Device_Property]] = None
	partNumber: Optional[str] = None
	modelNumber: Optional[str] = None
	type: CodeableConcept
	statusReason: Optional[List[CodeableConcept]] = None
	specialization: Optional[List[Device_Specialization]] = None
	distinctIdentifier: Optional[str] = None
	note: Optional[List[Annotation]] = None
	status: Optional[str] = None
	safety: Optional[List[CodeableConcept]] = None
	lotNumber: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	manufacturer: Optional[str] = None
	version: Optional[List[Device_Version]] = None
	location: Optional[Reference] = None
	contact: Optional[List[ContactPoint]] = None
	manufactureDate: Optional[str] = None
	owner: Optional[Reference] = None
	expirationDate: Optional[str] = None
	udiCarrier: Optional[List[Device_UdiCarrier]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None