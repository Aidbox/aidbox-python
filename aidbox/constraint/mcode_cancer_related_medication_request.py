from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class MedicationRequest_Substitution(BackboneElement):
	allowedBoolean: Optional[bool] = None
	allowedCodeableConcept: Optional[CodeableConcept] = None
	reason: Optional[CodeableConcept] = None

class MedicationRequest_DispenseRequest_InitialFill(BackboneElement):
	quantity: Optional[Quantity] = None
	duration: Optional[str] = None

class MedicationRequest_DispenseRequest(BackboneElement):
	initialFill: Optional[MedicationRequest_DispenseRequest_InitialFill] = None
	dispenseInterval: Optional[str] = None
	validityPeriod: Optional[Period] = None
	numberOfRepeatsAllowed: Optional[str] = None
	quantity: Optional[Quantity] = None
	expectedSupplyDuration: Optional[str] = None
	performer: Optional[Reference] = None

class McodeCancerRelatedMedicationRequest(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-cancer-related-medication-request"])
	performerType: Optional[CodeableConcept] = None
	category: Optional[List[CodeableConcept]] = None
	insurance: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	eventHistory: Optional[List[Reference]] = None
	instantiatesUri: Optional[List[str]] = None
	substitution: Optional[MedicationRequest_Substitution] = None
	detectedIssue: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	dispenseRequest: Optional[MedicationRequest_DispenseRequest] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: Optional[CodeableConcept] = None
	authoredOn: Optional[str] = None
	note: Optional[List[Annotation]] = None
	requester: Reference
	supportingInformation: Optional[List[Reference]] = None
	reportedReference: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	dosageInstruction: Optional[List[str]] = None
	groupIdentifier: Optional[Identifier] = None
	recorder: Optional[Reference] = None
	reportedBoolean: Optional[bool] = None
	identifier: Optional[List[Identifier]] = None
	doNotPerform: Optional[bool] = None
	intent: str
	basedOn: Optional[List[Reference]] = None
	priorPrescription: Optional[Reference] = None
	medicationReference: Optional[Reference] = None
	courseOfTherapyType: Optional[CodeableConcept] = None
	subject: Reference
	performer: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None