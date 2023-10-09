from typing import Optional
from ..base import *

class ChargeItemDefinition_PropertyGroup_PriceComponent(BackboneElement):
	amount: Optional[Money] = None
	code: Optional[CodeableConcept] = None
	factor: Optional[str] = None
	type: str

class ChargeItemDefinition_PropertyGroup(BackboneElement):
	applicability: list[str] = []
	priceComponent: list[ChargeItemDefinition_PropertyGroup_PriceComponent] = []

class ChargeItemDefinition_Applicability(BackboneElement):
	description: Optional[str] = None
	expression: Optional[str] = None
	language: Optional[str] = None

class ChargeItemDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	propertyGroup: list[ChargeItemDefinition_PropertyGroup] = []
	instance: list[Reference] = []
	jurisdiction: list[CodeableConcept] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	derivedFromUri: list[str] = []
	status: str
	url: str
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	replaces: list[str] = []
	partOf: list[str] = []
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	applicability: list[ChargeItemDefinition_Applicability] = []
	effectivePeriod: Optional[Period] = None

