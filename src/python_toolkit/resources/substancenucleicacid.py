from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class SubstanceNucleicAcid(DomainResource):
	areaOfHybridisation: Optional[str] = None
	numberOfSubunits: Optional[int] = None
	oligoNucleotideType: Optional[CodeableConcept] = None
	sequenceType: Optional[CodeableConcept] = None
	subunit: list[BackboneElement] = []

