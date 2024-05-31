from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductManufactured(DomainResource):
	manufacturedDoseForm: CodeableConcept
	unitOfPresentation: Optional[CodeableConcept] = None
	quantity: Quantity
	manufacturer: Optional[List[Reference]] = None
	ingredient: Optional[List[Reference]] = None
	physicalCharacteristics: Optional[ProdCharacteristic] = None
	otherCharacteristics: Optional[List[CodeableConcept]] = None