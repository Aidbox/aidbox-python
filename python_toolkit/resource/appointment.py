from typing import Optional
from ..base import *

class Appointment_Participant(BackboneElement):
	actor: Optional[Reference] = None
	period: Optional[Period] = None
	required: Optional[str] = None
	status: str
	type: list[CodeableConcept] = []

class Appointment(DomainResource):
	description: Optional[str] = None
	serviceCategory: list[CodeableConcept] = []
	slot: list[Reference] = []
	specialty: list[CodeableConcept] = []
	cancelationReason: Optional[CodeableConcept] = None
	requestedPeriod: list[Period] = []
	patientInstruction: Optional[str] = None
	start: Optional[str] = None
	reasonCode: list[CodeableConcept] = []
	created: Optional[str] = None
	participant: list[Appointment_Participant]
	serviceType: list[CodeableConcept] = []
	supportingInformation: list[Reference] = []
	priority: Optional[str] = None
	appointmentType: Optional[CodeableConcept] = None
	status: str
	comment: Optional[str] = None
	minutesDuration: Optional[str] = None
	identifier: list[Identifier] = []
	basedOn: list[Reference] = []
	end: Optional[str] = None
	reasonReference: list[Reference] = []

