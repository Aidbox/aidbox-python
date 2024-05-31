from pydantic import *
from typing import Optional, List
from ..base import *

class Appointment_Participant(BackboneElement):
	type: Optional[List[CodeableConcept]] = None
	actor: Optional[Reference] = None
	required: Optional[str] = None
	status: str
	period: Optional[Period] = None

class Appointment(DomainResource):
	description: Optional[str] = None
	serviceCategory: Optional[List[CodeableConcept]] = None
	slot: Optional[List[Reference]] = None
	specialty: Optional[List[CodeableConcept]] = None
	cancelationReason: Optional[CodeableConcept] = None
	requestedPeriod: Optional[List[Period]] = None
	patientInstruction: Optional[str] = None
	start: Optional[str] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	created: Optional[str] = None
	participant: List[Appointment_Participant]
	serviceType: Optional[List[CodeableConcept]] = None
	supportingInformation: Optional[List[Reference]] = None
	priority: Optional[NonNegativeInt] = None
	appointmentType: Optional[CodeableConcept] = None
	status: str
	comment: Optional[str] = None
	minutesDuration: Optional[PositiveInt] = None
	identifier: Optional[List[Identifier]] = None
	basedOn: Optional[List[Reference]] = None
	end: Optional[str] = None
	reasonReference: Optional[List[Reference]] = None