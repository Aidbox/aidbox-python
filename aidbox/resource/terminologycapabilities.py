from pydantic import *
from typing import Optional, List
from ..base import *

class TerminologyCapabilities_Expansion_Parameter(BackboneElement):
	name: str
	documentation: Optional[str] = None

class TerminologyCapabilities_Expansion(BackboneElement):
	hierarchical: Optional[bool] = None
	paging: Optional[bool] = None
	incomplete: Optional[bool] = None
	parameter: Optional[List[TerminologyCapabilities_Expansion_Parameter]] = None
	textFilter: Optional[str] = None

class TerminologyCapabilities_ValidateCode(BackboneElement):
	translations: bool

class TerminologyCapabilities_Translation(BackboneElement):
	needsMap: bool

class TerminologyCapabilities_CodeSystem_Version_Filter(BackboneElement):
	code: str
	op: List[str]

class TerminologyCapabilities_CodeSystem_Version(BackboneElement):
	code: Optional[str] = None
	isDefault: Optional[bool] = None
	compositional: Optional[bool] = None
	language: Optional[List[str]] = None
	filter: Optional[List[TerminologyCapabilities_CodeSystem_Version_Filter]] = None
	property: Optional[List[str]] = None

class TerminologyCapabilities_CodeSystem(BackboneElement):
	uri: Optional[str] = None
	version: Optional[List[TerminologyCapabilities_CodeSystem_Version]] = None
	subsumption: Optional[bool] = None

class TerminologyCapabilities_Software(BackboneElement):
	name: str
	version: Optional[str] = None

class TerminologyCapabilities_Implementation(BackboneElement):
	description: str
	url: Optional[str] = None

class TerminologyCapabilities_Closure(BackboneElement):
	translation: Optional[bool] = None

class TerminologyCapabilities(DomainResource):
	description: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	expansion: Optional[TerminologyCapabilities_Expansion] = None
	title: Optional[str] = None
	status: str
	validateCode: Optional[TerminologyCapabilities_ValidateCode] = None
	kind: str
	translation: Optional[TerminologyCapabilities_Translation] = None
	url: Optional[str] = None
	codeSystem: Optional[List[TerminologyCapabilities_CodeSystem]] = None
	software: Optional[TerminologyCapabilities_Software] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	implementation: Optional[TerminologyCapabilities_Implementation] = None
	codeSearch: Optional[str] = None
	lockedDate: Optional[bool] = None
	closure: Optional[TerminologyCapabilities_Closure] = None