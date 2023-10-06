from typing import Optional

from base import Reference
from base import Identifier
from base import Reference
from base import BackboneElement
from base import DomainResource


class ImmunizationRecommendation(DomainResource):
	authority: Optional[Reference] = None
	date: str
	identifier: list[Identifier] = []
	patient: Reference
	recommendation: list[BackboneElement]

