from typing import Optional
from base import *

class Encounter_Diagnosis(BackboneElement):
	condition: Reference
	rank: Optional[str] = None
	use: Optional[CodeableConcept] = None

class Encounter_Participant(BackboneElement):
	individual: Optional[Reference] = None
	period: Optional[Period] = None
	type: list[CodeableConcept] = []

class Encounter_ClassHistory(BackboneElement):
	class_: Coding
	period: Period

class Encounter_Hospitalization(BackboneElement):
	dischargeDisposition: Optional[CodeableConcept] = None
	preAdmissionIdentifier: Optional[Identifier] = None
	specialArrangement: list[CodeableConcept] = []
	dietPreference: list[CodeableConcept] = []
	admitSource: Optional[CodeableConcept] = None
	specialCourtesy: list[CodeableConcept] = []
	reAdmission: Optional[CodeableConcept] = None
	origin: Optional[Reference] = None
	destination: Optional[Reference] = None

class Encounter_Location(BackboneElement):
	location: Reference
	period: Optional[Period] = None
	physicalType: Optional[CodeableConcept] = None
	status: Optional[str] = None

class Encounter_StatusHistory(BackboneElement):
	period: Period
	status: str

class Encounter(DomainResource):
	appointment: list[Reference] = []
	diagnosis: list[Encounter_Diagnosis] = []
	serviceProvider: Optional[Reference] = None
	episodeOfCare: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	type: list[CodeableConcept] = []
	participant: list[Encounter_Participant] = []
	serviceType: Optional[CodeableConcept] = None
	account: list[Reference] = []
	classHistory: list[Encounter_ClassHistory] = []
	priority: Optional[CodeableConcept] = None
	status: str
	class_: Coding
	length: Optional[str] = None
	identifier: list[Identifier] = []
	hospitalization: Optional[Encounter_Hospitalization] = None
	period: Optional[Period] = None
	basedOn: list[Reference] = []
	partOf: Optional[Reference] = None
	location: list[Encounter_Location] = []
	subject: Optional[Reference] = None
	statusHistory: list[Encounter_StatusHistory] = []
	reasonReference: list[Reference] = []

