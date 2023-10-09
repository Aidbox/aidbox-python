from typing import Optional
from base import *

class Substance_Ingredient(BackboneElement):
	quantity: Optional[Ratio] = None
	substanceCodeableConcept: Optional[CodeableConcept] = None
	substanceReference: Optional[Reference] = None

class Substance_Instance(BackboneElement):
	expiry: Optional[str] = None
	identifier: Optional[Identifier] = None
	quantity: Optional[Quantity] = None

class Substance(DomainResource):
	category: list[CodeableConcept] = []
	code: CodeableConcept
	description: Optional[str] = None
	identifier: list[Identifier] = []
	ingredient: list[Substance_Ingredient] = []
	instance: list[Substance_Instance] = []
	status: Optional[str] = None

