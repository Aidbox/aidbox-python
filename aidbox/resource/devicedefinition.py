from pydantic import *
from typing import Optional, List
from ..base import *

class DeviceDefinition_DeviceName(BackboneElement):
	name: str
	type: str

class DeviceDefinition_Property(BackboneElement):
	type: CodeableConcept
	valueQuantity: Optional[List[Quantity]] = None
	valueCode: Optional[List[CodeableConcept]] = None

class DeviceDefinition_UdiDeviceIdentifier(BackboneElement):
	deviceIdentifier: str
	issuer: str
	jurisdiction: str

class DeviceDefinition_Capability(BackboneElement):
	type: CodeableConcept
	description: Optional[List[CodeableConcept]] = None

class DeviceDefinition_Specialization(BackboneElement):
	systemType: str
	version: Optional[str] = None

class DeviceDefinition_Material(BackboneElement):
	substance: CodeableConcept
	alternate: Optional[bool] = None
	allergenicIndicator: Optional[bool] = None

class DeviceDefinition(DomainResource):
	deviceName: Optional[List[DeviceDefinition_DeviceName]] = None
	shelfLifeStorage: Optional[List[ProductShelfLife]] = None
	property: Optional[List[DeviceDefinition_Property]] = None
	manufacturerString: Optional[str] = None
	modelNumber: Optional[str] = None
	udiDeviceIdentifier: Optional[List[DeviceDefinition_UdiDeviceIdentifier]] = None
	type: Optional[CodeableConcept] = None
	manufacturerReference: Optional[Reference] = None
	capability: Optional[List[DeviceDefinition_Capability]] = None
	specialization: Optional[List[DeviceDefinition_Specialization]] = None
	parentDevice: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	languageCode: Optional[List[CodeableConcept]] = None
	safety: Optional[List[CodeableConcept]] = None
	material: Optional[List[DeviceDefinition_Material]] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	quantity: Optional[Quantity] = None
	version: Optional[List[str]] = None
	contact: Optional[List[ContactPoint]] = None
	owner: Optional[Reference] = None
	onlineInformation: Optional[str] = None
	physicalCharacteristics: Optional[ProdCharacteristic] = None