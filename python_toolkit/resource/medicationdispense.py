from typing import Optional
from ..base import *

class MedicationDispense_Substitution(BackboneElement):
	reason: list[CodeableConcept] = []
	responsibleParty: list[Reference] = []
	type: Optional[CodeableConcept] = None
	wasSubstituted: bool

class MedicationDispense_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None

class MedicationDispense(DomainResource):
	statusReasonReference: Optional[Reference] = None
	category: Optional[CodeableConcept] = None
	whenHandedOver: Optional[str] = None
	whenPrepared: Optional[str] = None
	eventHistory: list[Reference] = []
	substitution: Optional[MedicationDispense_Substitution] = None
	detectedIssue: list[Reference] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	statusReasonCodeableConcept: Optional[CodeableConcept] = None
	supportingInformation: list[Reference] = []
	status: str
	dosageInstruction: list[str] = []
	daysSupply: Optional[Quantity] = None
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	partOf: list[Reference] = []
	location: Optional[Reference] = None
	authorizingPrescription: list[Reference] = []
	receiver: list[Reference] = []
	subject: Optional[Reference] = None
	destination: Optional[Reference] = None
	performer: list[MedicationDispense_Performer] = []

