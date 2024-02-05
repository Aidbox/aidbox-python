from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Encounter_Diagnosis(BackboneElement):
	condition: Reference
	use: Optional[CodeableConcept] = None
	rank: Optional[str] = None

class Encounter_Participant(BackboneElement):
	type: Optional[List[CodeableConcept]] = None
	period: Optional[Period] = None
	individual: Optional[Reference] = None

class Encounter_ClassHistory(BackboneElement):
	class_: Coding
	period: Period

class Encounter_Hospitalization(BackboneElement):
	dischargeDisposition: Optional[CodeableConcept] = None
	preAdmissionIdentifier: Optional[Identifier] = None
	specialArrangement: Optional[List[CodeableConcept]] = None
	dietPreference: Optional[List[CodeableConcept]] = None
	admitSource: Optional[CodeableConcept] = None
	specialCourtesy: Optional[List[CodeableConcept]] = None
	reAdmission: Optional[CodeableConcept] = None
	origin: Optional[Reference] = None
	destination: Optional[Reference] = None

class Encounter_Location(BackboneElement):
	location: Reference
	status: Optional[str] = None
	physicalType: Optional[CodeableConcept] = None
	period: Optional[Period] = None

class Encounter_StatusHistory(BackboneElement):
	status: str
	period: Period

class UsCoreEncounter(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"])
	appointment: Optional[List[Reference]] = None
	diagnosis: Optional[List[Encounter_Diagnosis]] = None
	serviceProvider: Optional[Reference] = None
	episodeOfCare: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	type: List[CodeableConcept]
	participant: Optional[List[Encounter_Participant]] = None
	serviceType: Optional[CodeableConcept] = None
	account: Optional[List[Reference]] = None
	classHistory: Optional[List[Encounter_ClassHistory]] = None
	priority: Optional[CodeableConcept] = None
	status: str
	class_: Coding
	length: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	hospitalization: Optional[Encounter_Hospitalization] = None
	period: Optional[Period] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[Reference] = None
	location: Optional[List[Encounter_Location]] = None
	subject: Reference
	statusHistory: Optional[List[Encounter_StatusHistory]] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None