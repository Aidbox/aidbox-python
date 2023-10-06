from typing import Optional

from base import CodeableConcept
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import ContactPoint
from base import Reference
from base import Period
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class OrganizationAffiliation(DomainResource):
	specialty: list[CodeableConcept] = []
	organization: Optional[Reference] = None
	participatingOrganization: Optional[Reference] = None
	active: Optional[bool] = None
	code: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	network: list[Reference] = []
	period: Optional[Period] = None
	location: list[Reference] = []
	endpoint: list[Reference] = []
	healthcareService: list[Reference] = []

