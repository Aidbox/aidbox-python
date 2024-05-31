from pydantic import *
from typing import Optional, List
from ..base import *

class Medication_Ingredient(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	isActive: Optional[bool] = None
	strength: Optional[Ratio] = None

class Medication_Batch(BackboneElement):
	lotNumber: Optional[str] = None
	expirationDate: Optional[str] = None

class Medication(DomainResource):
	identifier: Optional[List[Identifier]] = None
	code: Optional[CodeableConcept] = None
	status: Optional[str] = None
	manufacturer: Optional[Reference] = None
	form: Optional[CodeableConcept] = None
	amount: Optional[Ratio] = None
	ingredient: Optional[List[Medication_Ingredient]] = None
	batch: Optional[Medication_Batch] = None