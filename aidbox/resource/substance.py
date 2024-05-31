from pydantic import *
from typing import Optional, List
from ..base import *

class Substance_Instance(BackboneElement):
	identifier: Optional[Identifier] = None
	expiry: Optional[str] = None
	quantity: Optional[Quantity] = None

class Substance_Ingredient(BackboneElement):
	quantity: Optional[Ratio] = None
	substanceCodeableConcept: Optional[CodeableConcept] = None
	substanceReference: Optional[Reference] = None

class Substance(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: Optional[str] = None
	category: Optional[List[CodeableConcept]] = None
	code: CodeableConcept
	description: Optional[str] = None
	instance: Optional[List[Substance_Instance]] = None
	ingredient: Optional[List[Substance_Ingredient]] = None