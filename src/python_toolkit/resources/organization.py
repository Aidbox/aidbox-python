from typing import Optional

from base import Address
from base import CodeableConcept
from base import Identifier
from base import ContactPoint
from base import Reference
from base import Reference
from base import BackboneElement
from base import DomainResource


class Organization(DomainResource):
	address: list[Address] = []
	name: Optional[str] = None
	type: list[CodeableConcept] = []
	alias: list[str] = []
	active: Optional[bool] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	partOf: Optional[Reference] = None
	endpoint: list[Reference] = []
	contact: list[BackboneElement] = []

