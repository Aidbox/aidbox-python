from typing import Optional
from ..base import *

class CodeSystem_Property(BackboneElement):
	code: str
	description: Optional[str] = None
	type: str
	uri: Optional[str] = None

class CodeSystem_Filter(BackboneElement):
	code: str
	description: Optional[str] = None
	operator: list[str]
	value: str

class CodeSystem_Concept_Designation(BackboneElement):
	language: Optional[str] = None
	use: Optional[Coding] = None
	value: str

class CodeSystem_Concept_Property(BackboneElement):
	valueCode: Optional[str] = None
	valueDecimal: Optional[str] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueCoding: Optional[Coding] = None
	code: str
	valueInteger: Optional[int] = None

class CodeSystem_Concept(BackboneElement):
	code: str
	concept: list[str] = []
	definition: Optional[str] = None
	designation: list[CodeSystem_Concept_Designation] = []
	display: Optional[str] = None
	property: list[CodeSystem_Concept_Property] = []

class CodeSystem(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	versionNeeded: Optional[bool] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	content: str
	property: list[CodeSystem_Property] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	filter: list[CodeSystem_Filter] = []
	supplements: Optional[str] = None
	compositional: Optional[bool] = None
	status: str
	hierarchyMeaning: Optional[str] = None
	valueSet: Optional[str] = None
	count: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	concept: list[CodeSystem_Concept] = []
	caseSensitive: Optional[bool] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

