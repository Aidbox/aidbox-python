from typing import Optional

from base import Reference
from base import BackboneElement
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Reference
from base import Reference
from base import Period
from base import BackboneElement
from base import Reference
from base import BackboneElement
from base import DomainResource


class InsurancePlan(DomainResource):
	coverageArea: list[Reference] = []
	name: Optional[str] = None
	coverage: list[BackboneElement] = []
	type: list[CodeableConcept] = []
	alias: list[str] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	administeredBy: Optional[Reference] = None
	ownedBy: Optional[Reference] = None
	network: list[Reference] = []
	period: Optional[Period] = None
	plan: list[BackboneElement] = []
	endpoint: list[Reference] = []
	contact: list[BackboneElement] = []

