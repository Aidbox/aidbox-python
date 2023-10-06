from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import DomainResource


class MedicinalProductInteraction(DomainResource):
	description: Optional[str] = None
	effect: Optional[CodeableConcept] = None
	incidence: Optional[CodeableConcept] = None
	interactant: list[BackboneElement] = []
	management: Optional[CodeableConcept] = None
	subject: list[Reference] = []
	type: Optional[CodeableConcept] = None

