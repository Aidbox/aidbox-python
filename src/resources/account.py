from typing import Optional

from base import Period
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class Account(DomainResource):
	description: Optional[str] = None
	name: Optional[str] = None
	servicePeriod: Optional[Period] = None
	coverage: list[BackboneElement] = []
	type: Optional[CodeableConcept] = None
	guarantor: list[BackboneElement] = []
	status: str
	identifier: list[Identifier] = []
	partOf: Optional[Reference] = None
	subject: list[Reference] = []
	owner: Optional[Reference] = None

