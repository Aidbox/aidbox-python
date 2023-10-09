from typing import Optional
from ..base import *

class ValueSet_Compose_Include_Concept_Designation(BackboneElement):
	language: Optional[str] = None
	use: Optional[Coding] = None
	value: str

class ValueSet_Compose_Include_Concept(BackboneElement):
	code: str
	designation: list[ValueSet_Compose_Include_Concept_Designation] = []
	display: Optional[str] = None

class ValueSet_Compose_Include_Filter(BackboneElement):
	op: str
	property: str
	value: str

class ValueSet_Compose_Include(BackboneElement):
	concept: list[ValueSet_Compose_Include_Concept] = []
	filter: list[ValueSet_Compose_Include_Filter] = []
	system: Optional[str] = None
	valueSet: list[str] = []
	version: Optional[str] = None

class ValueSet_Compose(BackboneElement):
	exclude: list[str] = []
	inactive: Optional[bool] = None
	include: list[ValueSet_Compose_Include]
	lockedDate: Optional[str] = None

class ValueSet_Expansion_Contains(BackboneElement):
	abstract: Optional[bool] = None
	code: Optional[str] = None
	contains: list[str] = []
	designation: list[str] = []
	display: Optional[str] = None
	inactive: Optional[bool] = None
	system: Optional[str] = None
	version: Optional[str] = None

class ValueSet_Expansion_Parameter(BackboneElement):
	valueCode: Optional[str] = None
	valueUri: Optional[str] = None
	valueDecimal: Optional[str] = None
	name: str
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueInteger: Optional[int] = None

class ValueSet_Expansion(BackboneElement):
	contains: list[ValueSet_Expansion_Contains] = []
	identifier: Optional[str] = None
	offset: Optional[int] = None
	parameter: list[ValueSet_Expansion_Parameter] = []
	timestamp: str
	total: Optional[int] = None

class ValueSet(DomainResource):
	description: Optional[str] = None
	compose: Optional[ValueSet_Compose] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	expansion: Optional[ValueSet_Expansion] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	identifier: list[Identifier] = []
	immutable: Optional[bool] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

