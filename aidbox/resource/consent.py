from pydantic import *
from typing import Optional, List
from ..base import *

class Consent_Provision_Actor(BackboneElement):
	role: CodeableConcept
	reference: Reference

class Consent_Provision_Data(BackboneElement):
	meaning: str
	reference: Reference

class Consent_Provision(BackboneElement):
	provision: Optional[List[str]] = None
	purpose: Optional[List[Coding]] = None
	dataPeriod: Optional[Period] = None
	type: Optional[str] = None
	class_: Optional[List[Coding]] = None
	code: Optional[List[CodeableConcept]] = None
	action: Optional[List[CodeableConcept]] = None
	period: Optional[Period] = None
	securityLabel: Optional[List[Coding]] = None
	actor: Optional[List[Consent_Provision_Actor]] = None
	data: Optional[List[Consent_Provision_Data]] = None

class Consent_Verification(BackboneElement):
	verified: bool
	verifiedWith: Optional[Reference] = None
	verificationDate: Optional[str] = None

class Consent_Policy(BackboneElement):
	authority: Optional[str] = None
	uri: Optional[str] = None

class Consent(DomainResource):
	patient: Optional[Reference] = None
	category: List[CodeableConcept]
	provision: Optional[Consent_Provision] = None
	sourceAttachment: Optional[Attachment] = None
	organization: Optional[List[Reference]] = None
	verification: Optional[List[Consent_Verification]] = None
	scope: CodeableConcept
	policy: Optional[List[Consent_Policy]] = None
	sourceReference: Optional[Reference] = None
	dateTime: Optional[str] = None
	status: str
	policyRule: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	performer: Optional[List[Reference]] = None