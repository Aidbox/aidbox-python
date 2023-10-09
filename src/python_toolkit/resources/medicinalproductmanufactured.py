from typing import Optional
from base import *

class MedicinalProductManufactured(DomainResource):
	ingredient: list[Reference] = []
	manufacturedDoseForm: CodeableConcept
	manufacturer: list[Reference] = []
	otherCharacteristics: list[CodeableConcept] = []
	physicalCharacteristics: Optional[ProdCharacteristic] = None
	quantity: Quantity
	unitOfPresentation: Optional[CodeableConcept] = None

