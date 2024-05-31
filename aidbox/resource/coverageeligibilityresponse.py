from pydantic import *
from typing import Optional, List
from ..base import *

class CoverageEligibilityResponse_Insurance_Item_Benefit(BackboneElement):
	usedString: Optional[str] = None
	allowedMoney: Optional[Money] = None
	type: CodeableConcept
	allowedUnsignedInt: Optional[NonNegativeInt] = None
	usedUnsignedInt: Optional[NonNegativeInt] = None
	allowedString: Optional[str] = None
	usedMoney: Optional[Money] = None

class CoverageEligibilityResponse_Insurance_Item(BackboneElement):
	description: Optional[str] = None
	category: Optional[CodeableConcept] = None
	authorizationRequired: Optional[bool] = None
	modifier: Optional[List[CodeableConcept]] = None
	authorizationSupporting: Optional[List[CodeableConcept]] = None
	unit: Optional[CodeableConcept] = None
	excluded: Optional[bool] = None
	name: Optional[str] = None
	productOrService: Optional[CodeableConcept] = None
	term: Optional[CodeableConcept] = None
	benefit: Optional[List[CoverageEligibilityResponse_Insurance_Item_Benefit]] = None
	authorizationUrl: Optional[str] = None
	network: Optional[CodeableConcept] = None
	provider: Optional[Reference] = None

class CoverageEligibilityResponse_Insurance(BackboneElement):
	coverage: Reference
	inforce: Optional[bool] = None
	benefitPeriod: Optional[Period] = None
	item: Optional[List[CoverageEligibilityResponse_Insurance_Item]] = None

class CoverageEligibilityResponse_Error(BackboneElement):
	code: CodeableConcept

class CoverageEligibilityResponse(DomainResource):
	patient: Reference
	requestor: Optional[Reference] = None
	insurance: Optional[List[CoverageEligibilityResponse_Insurance]] = None
	request: Reference
	preAuthRef: Optional[str] = None
	purpose: List[str]
	created: str
	outcome: str
	disposition: Optional[str] = None
	insurer: Reference
	status: str
	servicedDate: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	error: Optional[List[CoverageEligibilityResponse_Error]] = None
	form: Optional[CodeableConcept] = None
	servicedPeriod: Optional[Period] = None