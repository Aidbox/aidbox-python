from typing import Optional
from base import *

class MedicinalProductPackaged_BatchIdentifier(BackboneElement):
	immediatePackaging: Optional[Identifier] = None
	outerPackaging: Identifier

class MedicinalProductPackaged_PackageItem(BackboneElement):
	manufacturedItem: list[Reference] = []
	otherCharacteristics: list[CodeableConcept] = []
	shelfLifeStorage: list[ProductShelfLife] = []
	alternateMaterial: list[CodeableConcept] = []
	type: CodeableConcept
	material: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	manufacturer: list[Reference] = []
	device: list[Reference] = []
	quantity: Quantity
	physicalCharacteristics: Optional[ProdCharacteristic] = None
	packageItem: list[str] = []

class MedicinalProductPackaged(DomainResource):
	description: Optional[str] = None
	marketingStatus: list[MarketingStatus] = []
	marketingAuthorization: Optional[Reference] = None
	identifier: list[Identifier] = []
	manufacturer: list[Reference] = []
	legalStatusOfSupply: Optional[CodeableConcept] = None
	batchIdentifier: list[MedicinalProductPackaged_BatchIdentifier] = []
	subject: list[Reference] = []
	packageItem: list[MedicinalProductPackaged_PackageItem]

