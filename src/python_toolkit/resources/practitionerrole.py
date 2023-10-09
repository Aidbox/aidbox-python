from typing import Optional
from base import *

class PractitionerRole_AvailableTime(BackboneElement):
	allDay: Optional[bool] = None
	availableEndTime: Optional[str] = None
	availableStartTime: Optional[str] = None
	daysOfWeek: list[str] = []

class PractitionerRole_NotAvailable(BackboneElement):
	description: str
	during: Optional[Period] = None

class PractitionerRole(DomainResource):
	availableTime: list[PractitionerRole_AvailableTime] = []
	specialty: list[CodeableConcept] = []
	notAvailable: list[PractitionerRole_NotAvailable] = []
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

