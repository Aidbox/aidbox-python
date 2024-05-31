from pydantic import *
from typing import Optional, List
from ..base import *

class VerificationResult_Validator(BackboneElement):
	organization: Reference
	identityCertificate: Optional[str] = None
	attestationSignature: Optional[Signature] = None

class VerificationResult_PrimarySource(BackboneElement):
	who: Optional[Reference] = None
	type: Optional[List[CodeableConcept]] = None
	communicationMethod: Optional[List[CodeableConcept]] = None
	validationStatus: Optional[CodeableConcept] = None
	validationDate: Optional[str] = None
	canPushUpdates: Optional[CodeableConcept] = None
	pushTypeAvailable: Optional[List[CodeableConcept]] = None

class VerificationResult_Attestation(BackboneElement):
	who: Optional[Reference] = None
	onBehalfOf: Optional[Reference] = None
	communicationMethod: Optional[CodeableConcept] = None
	date: Optional[str] = None
	sourceIdentityCertificate: Optional[str] = None
	proxyIdentityCertificate: Optional[str] = None
	proxySignature: Optional[Signature] = None
	sourceSignature: Optional[Signature] = None

class VerificationResult(DomainResource):
	failureAction: Optional[CodeableConcept] = None
	validationType: Optional[CodeableConcept] = None
	targetLocation: Optional[List[str]] = None
	validator: Optional[List[VerificationResult_Validator]] = None
	need: Optional[CodeableConcept] = None
	frequency: Optional[Timing] = None
	nextScheduled: Optional[str] = None
	primarySource: Optional[List[VerificationResult_PrimarySource]] = None
	attestation: Optional[VerificationResult_Attestation] = None
	status: str
	validationProcess: Optional[List[CodeableConcept]] = None
	statusDate: Optional[str] = None
	target: Optional[List[Reference]] = None
	lastPerformed: Optional[str] = None