from typing import Optional
from base import *

class Consent_Provision_Actor(BackboneElement):
	reference: Reference
	role: CodeableConcept

class Consent_Provision_Data(BackboneElement):
	meaning: str
	reference: Reference

class Consent_Provision(BackboneElement):
	provision: list[str] = []
	purpose: list[Coding] = []
	dataPeriod: Optional[Period] = None
	type: Optional[str] = None
	class_: list[Coding] = []
	code: list[CodeableConcept] = []
	action: list[CodeableConcept] = []
	period: Optional[Period] = None
	securityLabel: list[Coding] = []
	actor: list[Consent_Provision_Actor] = []
	data: list[Consent_Provision_Data] = []

class Consent_Verification(BackboneElement):
	verificationDate: Optional[str] = None
	verified: bool
	verifiedWith: Optional[Reference] = None

class Consent_Policy(BackboneElement):
	authority: Optional[str] = None
	uri: Optional[str] = None

class Consent(DomainResource):
	patient: Optional[Reference] = None
	category: list[CodeableConcept]
	provision: Optional[Consent_Provision] = None
	sourceAttachment: Optional[Attachment] = None
	organization: list[Reference] = []
	verification: list[Consent_Verification] = []
	scope: CodeableConcept
	policy: list[Consent_Policy] = []
	sourceReference: Optional[Reference] = None
	dateTime: Optional[str] = None
	status: str
	policyRule: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	performer: list[Reference] = []

