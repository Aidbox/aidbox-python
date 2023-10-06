from typing import Optional

from base import BackboneElement
from base import BackboneElement
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import DomainResource


class Group(DomainResource):
	name: Optional[str] = None
	type: str
	member: list[BackboneElement] = []
	characteristic: list[BackboneElement] = []
	active: Optional[bool] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	quantity: Optional[str] = None
	managingEntity: Optional[Reference] = None
	actual: bool

