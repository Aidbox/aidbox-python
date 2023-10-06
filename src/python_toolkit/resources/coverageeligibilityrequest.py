from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Period
from base import DomainResource


class CoverageEligibilityRequest(DomainResource):
	patient: Reference
	insurance: list[BackboneElement] = []
	facility: Optional[Reference] = None
	enterer: Optional[Reference] = None
	supportingInfo: list[BackboneElement] = []
	purpose: list[str]
	item: list[BackboneElement] = []
	created: str
	insurer: Reference
	priority: Optional[CodeableConcept] = None
	status: str
	servicedDate: Optional[str] = None
	identifier: list[Identifier] = []
	provider: Optional[Reference] = None
	servicedPeriod: Optional[Period] = None

