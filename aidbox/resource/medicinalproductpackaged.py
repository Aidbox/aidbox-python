from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductPackaged_BatchIdentifier(BackboneElement):
	outerPackaging: Identifier
	immediatePackaging: Optional[Identifier] = None

class MedicinalProductPackaged_PackageItem(BackboneElement):
	manufacturedItem: Optional[List[Reference]] = None
	otherCharacteristics: Optional[List[CodeableConcept]] = None
	shelfLifeStorage: Optional[List[ProductShelfLife]] = None
	alternateMaterial: Optional[List[CodeableConcept]] = None
	type: CodeableConcept
	material: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	manufacturer: Optional[List[Reference]] = None
	device: Optional[List[Reference]] = None
	quantity: Quantity
	physicalCharacteristics: Optional[ProdCharacteristic] = None
	packageItem: Optional[List[str]] = None

class MedicinalProductPackaged(DomainResource):
	description: Optional[str] = None
	marketingStatus: Optional[List[MarketingStatus]] = None
	marketingAuthorization: Optional[Reference] = None
	identifier: Optional[List[Identifier]] = None
	manufacturer: Optional[List[Reference]] = None
	legalStatusOfSupply: Optional[CodeableConcept] = None
	batchIdentifier: Optional[List[MedicinalProductPackaged_BatchIdentifier]] = None
	subject: Optional[List[Reference]] = None
	packageItem: List[MedicinalProductPackaged_PackageItem]