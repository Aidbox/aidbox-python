from typing import Optional
from ..base import *

class Medication_Batch(BackboneElement):
	expirationDate: Optional[str] = None
	lotNumber: Optional[str] = None

class Medication_Ingredient(BackboneElement):
	isActive: Optional[bool] = None
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	strength: Optional[Ratio] = None

class Medication(DomainResource):
	amount: Optional[Ratio] = None
	batch: Optional[Medication_Batch] = None
	code: Optional[CodeableConcept] = None
	form: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	ingredient: list[Medication_Ingredient] = []
	manufacturer: Optional[Reference] = None
	status: Optional[str] = None

