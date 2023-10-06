from typing import Optional

from base import Reference
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Quantity
from base import CodeableConcept
from base import ProdCharacteristic
from base import DomainResource


class MedicinalProductManufactured(DomainResource):
	ingredient: list[Reference] = []
	manufacturedDoseForm: CodeableConcept
	manufacturer: list[Reference] = []
	otherCharacteristics: list[CodeableConcept] = []
	physicalCharacteristics: Optional[ProdCharacteristic] = None
	quantity: Quantity
	unitOfPresentation: Optional[CodeableConcept] = None

