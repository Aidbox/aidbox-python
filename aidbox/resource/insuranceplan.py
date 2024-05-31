from pydantic import *
from typing import Optional, List
from ..base import *

class InsurancePlan_Coverage_Benefit_Limit(BackboneElement):
	value: Optional[Quantity] = None
	code: Optional[CodeableConcept] = None

class InsurancePlan_Coverage_Benefit(BackboneElement):
	type: CodeableConcept
	requirement: Optional[str] = None
	limit: Optional[List[InsurancePlan_Coverage_Benefit_Limit]] = None

class InsurancePlan_Coverage(BackboneElement):
	type: CodeableConcept
	network: Optional[List[Reference]] = None
	benefit: List[InsurancePlan_Coverage_Benefit]

class InsurancePlan_Plan_GeneralCost(BackboneElement):
	type: Optional[CodeableConcept] = None
	groupSize: Optional[PositiveInt] = None
	cost: Optional[Money] = None
	comment: Optional[str] = None

class InsurancePlan_Plan_SpecificCost_Benefit_Cost(BackboneElement):
	type: CodeableConcept
	applicability: Optional[CodeableConcept] = None
	qualifiers: Optional[List[CodeableConcept]] = None
	value: Optional[Quantity] = None

class InsurancePlan_Plan_SpecificCost_Benefit(BackboneElement):
	type: CodeableConcept
	cost: Optional[List[InsurancePlan_Plan_SpecificCost_Benefit_Cost]] = None

class InsurancePlan_Plan_SpecificCost(BackboneElement):
	category: CodeableConcept
	benefit: Optional[List[InsurancePlan_Plan_SpecificCost_Benefit]] = None

class InsurancePlan_Plan(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	type: Optional[CodeableConcept] = None
	coverageArea: Optional[List[Reference]] = None
	network: Optional[List[Reference]] = None
	generalCost: Optional[List[InsurancePlan_Plan_GeneralCost]] = None
	specificCost: Optional[List[InsurancePlan_Plan_SpecificCost]] = None

class InsurancePlan_Contact(BackboneElement):
	purpose: Optional[CodeableConcept] = None
	name: Optional[HumanName] = None
	telecom: Optional[List[ContactPoint]] = None
	address: Optional[Address] = None

class InsurancePlan(DomainResource):
	coverageArea: Optional[List[Reference]] = None
	name: Optional[str] = None
	coverage: Optional[List[InsurancePlan_Coverage]] = None
	type: Optional[List[CodeableConcept]] = None
	alias: Optional[List[str]] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	administeredBy: Optional[Reference] = None
	ownedBy: Optional[Reference] = None
	network: Optional[List[Reference]] = None
	period: Optional[Period] = None
	plan: Optional[List[InsurancePlan_Plan]] = None
	endpoint: Optional[List[Reference]] = None
	contact: Optional[List[InsurancePlan_Contact]] = None