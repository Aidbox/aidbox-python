from pydantic import *
from typing import Optional, List
from ..base import *

class MedicinalProductInteraction_Interactant(BackboneElement):
	itemReference: Optional[Reference] = None
	itemCodeableConcept: Optional[CodeableConcept] = None

class MedicinalProductInteraction(DomainResource):
	subject: Optional[List[Reference]] = None
	description: Optional[str] = None
	interactant: Optional[List[MedicinalProductInteraction_Interactant]] = None
	type: Optional[CodeableConcept] = None
	effect: Optional[CodeableConcept] = None
	incidence: Optional[CodeableConcept] = None
	management: Optional[CodeableConcept] = None