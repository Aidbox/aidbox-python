from typing import Optional
from ..base import *

class MedicationRequest_Substitution(BackboneElement):
	allowedBoolean: Optional[bool] = None
	allowedCodeableConcept: Optional[CodeableConcept] = None
	reason: Optional[CodeableConcept] = None

class MedicationRequest_DispenseRequest_InitialFill(BackboneElement):
	duration: Optional[str] = None
	quantity: Optional[Quantity] = None

class MedicationRequest_DispenseRequest(BackboneElement):
	dispenseInterval: Optional[str] = None
	expectedSupplyDuration: Optional[str] = None
	initialFill: Optional[MedicationRequest_DispenseRequest_InitialFill] = None
	numberOfRepeatsAllowed: Optional[str] = None
	performer: Optional[Reference] = None
	quantity: Optional[Quantity] = None
	validityPeriod: Optional[Period] = None

class MedicationRequest(DomainResource):
	performerType: Optional[CodeableConcept] = None
	category: list[CodeableConcept] = []
	insurance: list[Reference] = []
	instantiatesCanonical: list[str] = []
	eventHistory: list[Reference] = []
	instantiatesUri: list[str] = []
	substitution: Optional[MedicationRequest_Substitution] = None
	detectedIssue: list[Reference] = []
	encounter: Optional[Reference] = None
	dispenseRequest: Optional[MedicationRequest_DispenseRequest] = None
	reasonCode: list[CodeableConcept] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	note: list[Annotation] = []
	requester: Optional[Reference] = None
	supportingInformation: list[Reference] = []
	reportedReference: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	dosageInstruction: list[str] = []
	groupIdentifier: Optional[Identifier] = None
	recorder: Optional[Reference] = None
	reportedBoolean: Optional[bool] = None
	identifier: list[Identifier] = []
	doNotPerform: Optional[bool] = None
	intent: str
	basedOn: list[Reference] = []
	priorPrescription: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	courseOfTherapyType: Optional[CodeableConcept] = None
	subject: Reference
	performer: Optional[Reference] = None
	reasonReference: list[Reference] = []

