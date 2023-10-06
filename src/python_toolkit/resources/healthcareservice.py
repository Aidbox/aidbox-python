from typing import Optional

from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Attachment
from base import CodeableConcept
from base import Identifier
from base import CodeableConcept
from base import CodeableConcept
from base import ContactPoint
from base import Reference
from base import CodeableConcept
from base import Reference
from base import DomainResource


class HealthcareService(DomainResource):
	coverageArea: list[Reference] = []
	category: list[CodeableConcept] = []
	availableTime: list[BackboneElement] = []
	specialty: list[CodeableConcept] = []
	name: Optional[str] = None
	notAvailable: list[BackboneElement] = []
	providedBy: Optional[Reference] = None
	type: list[CodeableConcept] = []
	eligibility: list[BackboneElement] = []
	extraDetails: Optional[str] = None
	characteristic: list[CodeableConcept] = []
	photo: Optional[Attachment] = None
	active: Optional[bool] = None
	communication: list[CodeableConcept] = []
	comment: Optional[str] = None
	identifier: list[Identifier] = []
	serviceProvisionCode: list[CodeableConcept] = []
	availabilityExceptions: Optional[str] = None
	appointmentRequired: Optional[bool] = None
	referralMethod: list[CodeableConcept] = []
	telecom: list[ContactPoint] = []
	location: list[Reference] = []
	program: list[CodeableConcept] = []
	endpoint: list[Reference] = []

