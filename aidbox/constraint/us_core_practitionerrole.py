from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class PractitionerRole_AvailableTime(BackboneElement):
	daysOfWeek: Optional[List[str]] = None
	allDay: Optional[bool] = None
	availableStartTime: Optional[str] = None
	availableEndTime: Optional[str] = None

class PractitionerRole_NotAvailable(BackboneElement):
	description: str
	during: Optional[Period] = None

class UsCorePractitionerrole(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole"])
	availableTime: Optional[List[PractitionerRole_AvailableTime]] = None
	specialty: Optional[List[CodeableConcept]] = None
	notAvailable: Optional[List[PractitionerRole_NotAvailable]] = None
	organization: Optional[Reference] = None
	active: Optional[bool] = None
	code: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	availabilityExceptions: Optional[str] = None
	practitioner: Optional[Reference] = None
	telecom: Optional[List[ContactPoint]] = None
	period: Optional[Period] = None
	location: Optional[List[Reference]] = None
	endpoint: Optional[List[Reference]] = None
	healthcareService: Optional[List[Reference]] = None