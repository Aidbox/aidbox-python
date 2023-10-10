from typing import Optional
from ..base import *

class CoverageEligibilityRequest_Insurance(BackboneElement):
	businessArrangement: Optional[str] = None
	coverage: Reference
	focal: Optional[bool] = None

class CoverageEligibilityRequest_SupportingInfo(BackboneElement):
	appliesToAll: Optional[bool] = None
	information: Reference
	sequence: str

class CoverageEligibilityRequest_Item_Diagnosis(BackboneElement):
	diagnosisCodeableConcept: Optional[CodeableConcept] = None
	diagnosisReference: Optional[Reference] = None

class CoverageEligibilityRequest_Item(BackboneElement):
	category: Optional[CodeableConcept] = None
	facility: Optional[Reference] = None
	diagnosis: list[CoverageEligibilityRequest_Item_Diagnosis] = []
	modifier: list[CodeableConcept] = []
	productOrService: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	provider: Optional[Reference] = None
	supportingInfoSequence: list[str] = []
	unitPrice: Optional[Money] = None
	detail: list[Reference] = []

class CoverageEligibilityRequest(DomainResource):
	patient: Reference
	insurance: list[CoverageEligibilityRequest_Insurance] = []
	facility: Optional[Reference] = None
	enterer: Optional[Reference] = None
	supportingInfo: list[CoverageEligibilityRequest_SupportingInfo] = []
	purpose: list[str]
	item: list[CoverageEligibilityRequest_Item] = []
	created: str
	insurer: Reference
	priority: Optional[CodeableConcept] = None
	status: str
	servicedDate: Optional[str] = None
	identifier: list[Identifier] = []
	provider: Optional[Reference] = None
	servicedPeriod: Optional[Period] = None

