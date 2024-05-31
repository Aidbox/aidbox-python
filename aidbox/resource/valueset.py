from pydantic import *
from typing import Optional, List
from ..base import *

class ValueSet_Compose_Include_Concept_Designation(BackboneElement):
	language: Optional[str] = None
	use: Optional[Coding] = None
	value: str

class ValueSet_Compose_Include_Concept(BackboneElement):
	code: str
	display: Optional[str] = None
	designation: Optional[List[ValueSet_Compose_Include_Concept_Designation]] = None

class ValueSet_Compose_Include_Filter(BackboneElement):
	property: str
	op: str
	value: str

class ValueSet_Compose_Include(BackboneElement):
	system: Optional[str] = None
	version: Optional[str] = None
	concept: Optional[List[ValueSet_Compose_Include_Concept]] = None
	filter: Optional[List[ValueSet_Compose_Include_Filter]] = None
	valueSet: Optional[List[str]] = None

class ValueSet_Compose(BackboneElement):
	lockedDate: Optional[str] = None
	inactive: Optional[bool] = None
	include: List[ValueSet_Compose_Include]
	exclude: Optional[List[str]] = None

class ValueSet_Expansion_Parameter(BackboneElement):
	valueCode: Optional[str] = None
	valueUri: Optional[str] = None
	valueDecimal: Optional[float] = None
	name: str
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueInteger: Optional[int] = None

class ValueSet_Expansion_Contains(BackboneElement):
	system: Optional[str] = None
	abstract: Optional[bool] = None
	inactive: Optional[bool] = None
	version: Optional[str] = None
	code: Optional[str] = None
	display: Optional[str] = None
	designation: Optional[List[str]] = None
	contains: Optional[List[str]] = None

class ValueSet_Expansion(BackboneElement):
	identifier: Optional[str] = None
	timestamp: str
	total: Optional[int] = None
	offset: Optional[int] = None
	parameter: Optional[List[ValueSet_Expansion_Parameter]] = None
	contains: Optional[List[ValueSet_Expansion_Contains]] = None

class ValueSet(DomainResource):
	description: Optional[str] = None
	compose: Optional[ValueSet_Compose] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	expansion: Optional[ValueSet_Expansion] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	immutable: Optional[bool] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None