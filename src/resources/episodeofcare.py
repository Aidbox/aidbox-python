from typing import Optional

from base import Reference
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Reference
from base import Reference
from base import Identifier
from base import Period
from base import Reference
from base import BackboneElement
from base import DomainResource


class EpisodeOfCare(DomainResource):
	patient: Reference
	diagnosis: list[BackboneElement] = []
	managingOrganization: Optional[Reference] = None
	type: list[CodeableConcept] = []
	account: list[Reference] = []
	referralRequest: list[Reference] = []
	team: list[Reference] = []
	status: str
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	careManager: Optional[Reference] = None
	statusHistory: list[BackboneElement] = []

