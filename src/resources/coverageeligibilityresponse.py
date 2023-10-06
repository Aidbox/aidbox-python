from typing import Optional

from base import Reference
from base import Reference
from base import BackboneElement
from base import Reference
from base import Reference
from base import Identifier
from base import BackboneElement
from base import CodeableConcept
from base import Period
from base import DomainResource


class CoverageEligibilityResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	insurance: list[BackboneElement] = []
	request: Reference
	preAuthRef: Optional[str] = None
	purpose: list[str]
	created: str
	outcome: str
	disposition: Optional[str] = None
	insurer: Reference
	status: str
	servicedDate: Optional[str] = None
	identifier: list[Identifier] = []
	error: list[BackboneElement] = []
	form: Optional[CodeableConcept] = None
	servicedPeriod: Optional[Period] = None

