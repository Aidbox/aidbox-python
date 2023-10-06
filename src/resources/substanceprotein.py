from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class SubstanceProtein(DomainResource):
	disulfideLinkage: list[str] = []
	numberOfSubunits: Optional[int] = None
	sequenceType: Optional[CodeableConcept] = None
	subunit: list[BackboneElement] = []

