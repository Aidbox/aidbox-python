from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class SubstancePolymer(DomainResource):
	class_: Optional[CodeableConcept] = None
	copolymerConnectivity: list[CodeableConcept] = []
	geometry: Optional[CodeableConcept] = None
	modification: list[str] = []
	monomerSet: list[BackboneElement] = []
	repeat: list[BackboneElement] = []

