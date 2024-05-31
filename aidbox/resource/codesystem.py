from pydantic import *
from typing import Optional, List
from ..base import *

class CodeSystem_Property(BackboneElement):
	code: str
	uri: Optional[str] = None
	description: Optional[str] = None
	type: str

class CodeSystem_Filter(BackboneElement):
	code: str
	description: Optional[str] = None
	operator: List[str]
	value: str

class CodeSystem_Concept_Designation(BackboneElement):
	language: Optional[str] = None
	use: Optional[Coding] = None
	value: str

class CodeSystem_Concept_Property(BackboneElement):
	valueCode: Optional[str] = None
	valueDecimal: Optional[float] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueCoding: Optional[Coding] = None
	code: str
	valueInteger: Optional[int] = None

class CodeSystem_Concept(BackboneElement):
	code: str
	display: Optional[str] = None
	definition: Optional[str] = None
	designation: Optional[List[CodeSystem_Concept_Designation]] = None
	property: Optional[List[CodeSystem_Concept_Property]] = None
	concept: Optional[List[str]] = None

class CodeSystem(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	versionNeeded: Optional[bool] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	content: str
	property: Optional[List[CodeSystem_Property]] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	filter: Optional[List[CodeSystem_Filter]] = None
	supplements: Optional[str] = None
	compositional: Optional[bool] = None
	status: str
	hierarchyMeaning: Optional[str] = None
	valueSet: Optional[str] = None
	count: Optional[NonNegativeInt] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	concept: Optional[List[CodeSystem_Concept]] = None
	caseSensitive: Optional[bool] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None