from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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
	valueDecimal: Optional[str] = None
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

class Shareablecodesystem(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/shareablecodesystem"])
	description: str
	date: Optional[str] = None
	versionNeeded: Optional[bool] = None
	publisher: str
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	content: str
	property: Optional[List[CodeSystem_Property]] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: bool
	title: Optional[str] = None
	filter: Optional[List[CodeSystem_Filter]] = None
	supplements: Optional[str] = None
	compositional: Optional[bool] = None
	status: str
	hierarchyMeaning: Optional[str] = None
	valueSet: Optional[str] = None
	count: Optional[str] = None
	url: str
	identifier: Optional[List[Identifier]] = None
	concept: List[CodeSystem_Concept]
	caseSensitive: Optional[bool] = None
	version: str
	contact: Optional[List[ContactDetail]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None