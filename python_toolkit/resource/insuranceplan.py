from typing import Optional
from ..base import *

class InsurancePlan_Coverage_Benefit_Limit(BackboneElement):
	code: Optional[CodeableConcept] = None
	value: Optional[Quantity] = None

class InsurancePlan_Coverage_Benefit(BackboneElement):
	limit: list[InsurancePlan_Coverage_Benefit_Limit] = []
	requirement: Optional[str] = None
	type: CodeableConcept

class InsurancePlan_Coverage(BackboneElement):
	benefit: list[InsurancePlan_Coverage_Benefit]
	network: list[Reference] = []
	type: CodeableConcept

class InsurancePlan_Plan_GeneralCost(BackboneElement):
	comment: Optional[str] = None
	cost: Optional[Money] = None
	groupSize: Optional[str] = None
	type: Optional[CodeableConcept] = None

class InsurancePlan_Plan_SpecificCost_Benefit_Cost(BackboneElement):
	applicability: Optional[CodeableConcept] = None
	qualifiers: list[CodeableConcept] = []
	type: CodeableConcept
	value: Optional[Quantity] = None

class InsurancePlan_Plan_SpecificCost_Benefit(BackboneElement):
	cost: list[InsurancePlan_Plan_SpecificCost_Benefit_Cost] = []
	type: CodeableConcept

class InsurancePlan_Plan_SpecificCost(BackboneElement):
	benefit: list[InsurancePlan_Plan_SpecificCost_Benefit] = []
	category: CodeableConcept

class InsurancePlan_Plan(BackboneElement):
	coverageArea: list[Reference] = []
	generalCost: list[InsurancePlan_Plan_GeneralCost] = []
	identifier: list[Identifier] = []
	network: list[Reference] = []
	specificCost: list[InsurancePlan_Plan_SpecificCost] = []
	type: Optional[CodeableConcept] = None

class InsurancePlan_Contact(BackboneElement):
	address: Optional[Address] = None
	name: Optional[HumanName] = None
	purpose: Optional[CodeableConcept] = None
	telecom: list[ContactPoint] = []

class InsurancePlan(DomainResource):
	coverageArea: list[Reference] = []
	name: Optional[str] = None
	coverage: list[InsurancePlan_Coverage] = []
	type: list[CodeableConcept] = []
	alias: list[str] = []
	status: Optional[str] = None
	identifier: list[Identifier] = []
	administeredBy: Optional[Reference] = None
	ownedBy: Optional[Reference] = None
	network: list[Reference] = []
	period: Optional[Period] = None
	plan: list[InsurancePlan_Plan] = []
	endpoint: list[Reference] = []
	contact: list[InsurancePlan_Contact] = []

