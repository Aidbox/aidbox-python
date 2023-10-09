from typing import Optional
from base import *

class VerificationResult_Validator(BackboneElement):
	attestationSignature: Optional[Signature] = None
	identityCertificate: Optional[str] = None
	organization: Reference

class VerificationResult_PrimarySource(BackboneElement):
	canPushUpdates: Optional[CodeableConcept] = None
	communicationMethod: list[CodeableConcept] = []
	pushTypeAvailable: list[CodeableConcept] = []
	type: list[CodeableConcept] = []
	validationDate: Optional[str] = None
	validationStatus: Optional[CodeableConcept] = None
	who: Optional[Reference] = None

class VerificationResult_Attestation(BackboneElement):
	communicationMethod: Optional[CodeableConcept] = None
	date: Optional[str] = None
	onBehalfOf: Optional[Reference] = None
	proxyIdentityCertificate: Optional[str] = None
	proxySignature: Optional[Signature] = None
	sourceIdentityCertificate: Optional[str] = None
	sourceSignature: Optional[Signature] = None
	who: Optional[Reference] = None

class VerificationResult(DomainResource):
	failureAction: Optional[CodeableConcept] = None
	validationType: Optional[CodeableConcept] = None
	targetLocation: list[str] = []
	validator: list[VerificationResult_Validator] = []
	need: Optional[CodeableConcept] = None
	frequency: Optional[str] = None
	nextScheduled: Optional[str] = None
	primarySource: list[VerificationResult_PrimarySource] = []
	attestation: Optional[VerificationResult_Attestation] = None
	status: str
	validationProcess: list[CodeableConcept] = []
	statusDate: Optional[str] = None
	target: list[Reference] = []
	lastPerformed: Optional[str] = None

