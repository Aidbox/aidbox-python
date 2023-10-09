from typing import Optional
from base import *

class CoverageEligibilityResponse_Insurance_Item_Benefit(BackboneElement):
	usedString: Optional[str] = None
	allowedMoney: Optional[Money] = None
	type: CodeableConcept
	allowedUnsignedInt: Optional[str] = None
	usedUnsignedInt: Optional[str] = None
	allowedString: Optional[str] = None
	usedMoney: Optional[Money] = None

class CoverageEligibilityResponse_Insurance_Item(BackboneElement):
	description: Optional[str] = None
	category: Optional[CodeableConcept] = None
	authorizationRequired: Optional[bool] = None
	modifier: list[CodeableConcept] = []
	authorizationSupporting: list[CodeableConcept] = []
	unit: Optional[CodeableConcept] = None
	excluded: Optional[bool] = None
	name: Optional[str] = None
	productOrService: Optional[CodeableConcept] = None
	term: Optional[CodeableConcept] = None
	benefit: list[CoverageEligibilityResponse_Insurance_Item_Benefit] = []
	authorizationUrl: Optional[str] = None
	network: Optional[CodeableConcept] = None
	provider: Optional[Reference] = None

class CoverageEligibilityResponse_Insurance(BackboneElement):
	benefitPeriod: Optional[Period] = None
	coverage: Reference
	inforce: Optional[bool] = None
	item: list[CoverageEligibilityResponse_Insurance_Item] = []

class CoverageEligibilityResponse_Error(BackboneElement):
	code: CodeableConcept

class CoverageEligibilityResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	insurance: list[CoverageEligibilityResponse_Insurance] = []
	request: Reference
	preAuthRef: Optional[str] = None
	purpose: list[str]
	created: str
	outcome: str
	disposition: Optional[str] = None
	insurer: Reference
	status: str
	servicedDate: Optional[str] = None
	identifier: list[Identifier] = []
	error: list[CoverageEligibilityResponse_Error] = []
	form: Optional[CodeableConcept] = None
	servicedPeriod: Optional[Period] = None

