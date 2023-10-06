from typing import Optional

from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Period
from base import CodeableConcept
from base import BackboneElement
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import Identifier
from base import Reference
from base import Reference
from base import DomainResource


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
	participant: list[BackboneElement]
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

