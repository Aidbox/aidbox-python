from pydantic import *
from typing import Optional, List
from ..base import *

class MedicationDispense_Substitution(BackboneElement):
	wasSubstituted: bool
	type: Optional[CodeableConcept] = None
	reason: Optional[List[CodeableConcept]] = None
	responsibleParty: Optional[List[Reference]] = None

class MedicationDispense_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference

class MedicationDispense(DomainResource):
	statusReasonReference: Optional[Reference] = None
	category: Optional[CodeableConcept] = None
	whenHandedOver: Optional[str] = None
	whenPrepared: Optional[str] = None
	eventHistory: Optional[List[Reference]] = None
	substitution: Optional[MedicationDispense_Substitution] = None
	detectedIssue: Optional[List[Reference]] = None
	medicationCodeableConcept: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	note: Optional[List[Annotation]] = None
	statusReasonCodeableConcept: Optional[CodeableConcept] = None
	supportingInformation: Optional[List[Reference]] = None
	status: str
	dosageInstruction: Optional[List[Dosage]] = None
	daysSupply: Optional[Quantity] = None
	identifier: Optional[List[Identifier]] = None
	context: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	partOf: Optional[List[Reference]] = None
	location: Optional[Reference] = None
	authorizingPrescription: Optional[List[Reference]] = None
	receiver: Optional[List[Reference]] = None
	subject: Optional[Reference] = None
	destination: Optional[Reference] = None
	performer: Optional[List[MedicationDispense_Performer]] = None