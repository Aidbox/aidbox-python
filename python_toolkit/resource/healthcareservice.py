from typing import Optional
from ..base import *

class HealthcareService_AvailableTime(BackboneElement):
	allDay: Optional[bool] = None
	availableEndTime: Optional[str] = None
	availableStartTime: Optional[str] = None
	daysOfWeek: list[str] = []

class HealthcareService_NotAvailable(BackboneElement):
	description: str
	during: Optional[Period] = None

class HealthcareService_Eligibility(BackboneElement):
	code: Optional[CodeableConcept] = None
	comment: Optional[str] = None

class HealthcareService(DomainResource):
	coverageArea: list[Reference] = []
	category: list[CodeableConcept] = []
	availableTime: list[HealthcareService_AvailableTime] = []
	specialty: list[CodeableConcept] = []
	name: Optional[str] = None
	notAvailable: list[HealthcareService_NotAvailable] = []
	providedBy: Optional[Reference] = None
	type: list[CodeableConcept] = []
	eligibility: list[HealthcareService_Eligibility] = []
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

