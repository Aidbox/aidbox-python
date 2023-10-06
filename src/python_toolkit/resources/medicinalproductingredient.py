from typing import Optional

from base import Identifier
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class MedicinalProductIngredient(DomainResource):
	allergenicIndicator: Optional[bool] = None
	identifier: Optional[Identifier] = None
	manufacturer: list[Reference] = []
	role: CodeableConcept
	specifiedSubstance: list[BackboneElement] = []
	substance: Optional[BackboneElement] = None

