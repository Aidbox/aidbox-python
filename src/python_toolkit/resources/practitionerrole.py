from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import ContactPoint
from base import Period
from base import Reference
from base import Reference
from base import Reference
from base import DomainResource


class PractitionerRole(DomainResource):
	availableTime: list[BackboneElement] = []
	specialty: list[CodeableConcept] = []
	notAvailable: list[BackboneElement] = []
	organization: Optional[Reference] = None
	active: Optional[bool] = None
	code: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	availabilityExceptions: Optional[str] = None
	practitioner: Optional[Reference] = None
	telecom: list[ContactPoint] = []
	period: Optional[Period] = None
	location: list[Reference] = []
	endpoint: list[Reference] = []
	healthcareService: list[Reference] = []

