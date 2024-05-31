from pydantic import *
from typing import Optional, List
from ..base import *

class HealthcareService_AvailableTime(BackboneElement):
	daysOfWeek: Optional[List[str]] = None
	allDay: Optional[bool] = None
	availableStartTime: Optional[str] = None
	availableEndTime: Optional[str] = None

class HealthcareService_NotAvailable(BackboneElement):
	description: str
	during: Optional[Period] = None

class HealthcareService_Eligibility(BackboneElement):
	code: Optional[CodeableConcept] = None
	comment: Optional[str] = None

class HealthcareService(DomainResource):
	coverageArea: Optional[List[Reference]] = None
	category: Optional[List[CodeableConcept]] = None
	availableTime: Optional[List[HealthcareService_AvailableTime]] = None
	specialty: Optional[List[CodeableConcept]] = None
	name: Optional[str] = None
	notAvailable: Optional[List[HealthcareService_NotAvailable]] = None
	providedBy: Optional[Reference] = None
	type: Optional[List[CodeableConcept]] = None
	eligibility: Optional[List[HealthcareService_Eligibility]] = None
	extraDetails: Optional[str] = None
	characteristic: Optional[List[CodeableConcept]] = None
	photo: Optional[Attachment] = None
	active: Optional[bool] = None
	communication: Optional[List[CodeableConcept]] = None
	comment: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	serviceProvisionCode: Optional[List[CodeableConcept]] = None
	availabilityExceptions: Optional[str] = None
	appointmentRequired: Optional[bool] = None
	referralMethod: Optional[List[CodeableConcept]] = None
	telecom: Optional[List[ContactPoint]] = None
	location: Optional[List[Reference]] = None
	program: Optional[List[CodeableConcept]] = None
	endpoint: Optional[List[Reference]] = None