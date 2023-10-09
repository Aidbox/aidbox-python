from typing import Optional
from base import *

class MedicinalProductInteraction_Interactant(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None

class MedicinalProductInteraction(DomainResource):
	description: Optional[str] = None
	effect: Optional[CodeableConcept] = None
	incidence: Optional[CodeableConcept] = None
	interactant: list[MedicinalProductInteraction_Interactant] = []
	management: Optional[CodeableConcept] = None
	subject: list[Reference] = []
	type: Optional[CodeableConcept] = None

