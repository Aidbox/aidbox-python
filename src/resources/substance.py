from typing import Optional

from base import CodeableConcept
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class Substance(DomainResource):
	category: list[CodeableConcept] = []
	code: CodeableConcept
	description: Optional[str] = None
	identifier: list[Identifier] = []
	ingredient: list[BackboneElement] = []
	instance: list[BackboneElement] = []
	status: Optional[str] = None

