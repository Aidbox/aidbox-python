from typing import Optional
from base import *

class Coverage_CostToBeneficiary_Exception(BackboneElement):
	period: Optional[Period] = None
	type: CodeableConcept

class Coverage_CostToBeneficiary(BackboneElement):
	exception: list[Coverage_CostToBeneficiary_Exception] = []
	type: Optional[CodeableConcept] = None
	valueMoney: Optional[Money] = None
	valueQuantity: Optional[Quantity] = None

class Coverage_Class(BackboneElement):
	name: Optional[str] = None
	type: CodeableConcept
	value: str

class Coverage(DomainResource):
	policyHolder: Optional[Reference] = None
	beneficiary: Reference
	contract: list[Reference] = []
	relationship: Optional[CodeableConcept] = None
	type: Optional[CodeableConcept] = None
	costToBeneficiary: list[Coverage_CostToBeneficiary] = []
	subrogation: Optional[bool] = None
	subscriber: Optional[Reference] = None
	payor: list[Reference]
	status: str
	class_: list[Coverage_Class] = []
	identifier: list[Identifier] = []
	order: Optional[str] = None
	network: Optional[str] = None
	period: Optional[Period] = None
	dependent: Optional[str] = None
	subscriberId: Optional[str] = None

