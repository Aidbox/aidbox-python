from typing import Optional

from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class SpecimenDefinition(DomainResource):
	collection: list[CodeableConcept] = []
	identifier: Optional[Identifier] = None
	patientPreparation: list[CodeableConcept] = []
	timeAspect: Optional[str] = None
	typeCollected: Optional[CodeableConcept] = None
	typeTested: list[BackboneElement] = []

