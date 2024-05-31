from pydantic import *
from typing import Optional, List
from ..base import *

class Coverage_CostToBeneficiary_Exception(BackboneElement):
	type: CodeableConcept
	period: Optional[Period] = None

class Coverage_CostToBeneficiary(BackboneElement):
	type: Optional[CodeableConcept] = None
	valueQuantity: Optional[Quantity] = None
	valueMoney: Optional[Money] = None
	exception: Optional[List[Coverage_CostToBeneficiary_Exception]] = None

class Coverage_Class(BackboneElement):
	type: CodeableConcept
	value: str
	name: Optional[str] = None

class Coverage(DomainResource):
	policyHolder: Optional[Reference] = None
	beneficiary: Reference
	contract: Optional[List[Reference]] = None
	relationship: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	costToBeneficiary: Optional[List[Coverage_CostToBeneficiary]] = None
	subrogation: Optional[bool] = None
	subscriber: Optional[Reference] = None
	payor: List[Reference]
	status: str
	class_: Optional[List[Coverage_Class]] = None
	identifier: Optional[List[Identifier]] = None
	order: Optional[PositiveInt] = None
	network: Optional[str] = None
	period: Optional[Period] = None
	dependent: Optional[str] = None
	subscriberId: Optional[str] = None