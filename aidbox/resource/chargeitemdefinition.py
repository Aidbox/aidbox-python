from pydantic import *
from typing import Optional, List
from ..base import *

class ChargeItemDefinition_PropertyGroup_PriceComponent(BackboneElement):
	type: str
	code: Optional[CodeableConcept] = None
	factor: Optional[float] = None
	amount: Optional[Money] = None

class ChargeItemDefinition_PropertyGroup(BackboneElement):
	applicability: Optional[List[str]] = None
	priceComponent: Optional[List[ChargeItemDefinition_PropertyGroup_PriceComponent]] = None

class ChargeItemDefinition_Applicability(BackboneElement):
	description: Optional[str] = None
	language: Optional[str] = None
	expression: Optional[str] = None

class ChargeItemDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	propertyGroup: Optional[List[ChargeItemDefinition_PropertyGroup]] = None
	instance: Optional[List[Reference]] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	derivedFromUri: Optional[List[str]] = None
	status: str
	url: str
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	replaces: Optional[List[str]] = None
	partOf: Optional[List[str]] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	applicability: Optional[List[ChargeItemDefinition_Applicability]] = None
	effectivePeriod: Optional[Period] = None