from typing import Optional
from ..base import *

class DeviceDefinition_DeviceName(BackboneElement):
	name: str
	type: str

class DeviceDefinition_Property(BackboneElement):
	type: CodeableConcept
	valueCode: list[CodeableConcept] = []
	valueQuantity: list[Quantity] = []

class DeviceDefinition_UdiDeviceIdentifier(BackboneElement):
	deviceIdentifier: str
	issuer: str
	jurisdiction: str

class DeviceDefinition_Capability(BackboneElement):
	description: list[CodeableConcept] = []
	type: CodeableConcept

class DeviceDefinition_Specialization(BackboneElement):
	systemType: str
	version: Optional[str] = None

class DeviceDefinition_Material(BackboneElement):
	allergenicIndicator: Optional[bool] = None
	alternate: Optional[bool] = None
	substance: CodeableConcept

class DeviceDefinition(DomainResource):
	deviceName: list[DeviceDefinition_DeviceName] = []
	shelfLifeStorage: list[ProductShelfLife] = []
	property: list[DeviceDefinition_Property] = []
	manufacturerString: Optional[str] = None
	modelNumber: Optional[str] = None
	udiDeviceIdentifier: list[DeviceDefinition_UdiDeviceIdentifier] = []
	type: Optional[CodeableConcept] = None
	manufacturerReference: Optional[Reference] = None
	capability: list[DeviceDefinition_Capability] = []
	specialization: list[DeviceDefinition_Specialization] = []
	parentDevice: Optional[Reference] = None
	note: list[Annotation] = []
	languageCode: list[CodeableConcept] = []
	safety: list[CodeableConcept] = []
	material: list[DeviceDefinition_Material] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	quantity: Optional[Quantity] = None
	version: list[str] = []
	contact: list[ContactPoint] = []
	owner: Optional[Reference] = None
	onlineInformation: Optional[str] = None
	physicalCharacteristics: Optional[ProdCharacteristic] = None

