from pydantic import *
from typing import Optional, List
from ..base import *

class CoverageEligibilityRequest_Insurance(BackboneElement):
	focal: Optional[bool] = None
	coverage: Reference
	businessArrangement: Optional[str] = None

class CoverageEligibilityRequest_SupportingInfo(BackboneElement):
	sequence: PositiveInt
	information: Reference
	appliesToAll: Optional[bool] = None

class CoverageEligibilityRequest_Item_Diagnosis(BackboneElement):
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None

class CoverageEligibilityRequest_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	facility: Optional[Reference] = None
	diagnosis: Optional[List[CoverageEligibilityRequest_Item_Diagnosis]] = None
	modifier: Optional[List[CodeableConcept]] = None
	productOrService: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: Optional[Reference] = None
	supportingInfoSequence: Optional[List[PositiveInt]] = None
	unitPrice: Optional[Money] = None
	detail: Optional[List[Reference]] = None

class CoverageEligibilityRequest(DomainResource):
	patient: Reference
	insurance: Optional[List[CoverageEligibilityRequest_Insurance]] = None
	facility: Optional[Reference] = None
	enterer: Optional[Reference] = None
	supportingInfo: Optional[List[CoverageEligibilityRequest_SupportingInfo]] = None
	purpose: List[str]
	item: Optional[List[CoverageEligibilityRequest_Item]] = None
	created: str
	insurer: Reference
	priority: Optional[CodeableConcept] = None
	status: str
	servicedDate: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	provider: Optional[Reference] = None
	servicedPeriod: Optional[Period] = None