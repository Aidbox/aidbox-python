from typing import Optional

from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class SubstanceReferenceInformation(DomainResource):
	classification: list[BackboneElement] = []
	comment: Optional[str] = None
	gene: list[BackboneElement] = []
	geneElement: list[BackboneElement] = []
	target: list[BackboneElement] = []

