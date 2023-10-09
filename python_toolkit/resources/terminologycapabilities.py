from typing import Optional
from base import *

class TerminologyCapabilities_Expansion_Parameter(BackboneElement):
	documentation: Optional[str] = None
	name: str

class TerminologyCapabilities_Expansion(BackboneElement):
	hierarchical: Optional[bool] = None
	incomplete: Optional[bool] = None
	paging: Optional[bool] = None
	parameter: list[TerminologyCapabilities_Expansion_Parameter] = []
	textFilter: Optional[str] = None

class TerminologyCapabilities_ValidateCode(BackboneElement):
	translations: bool

class TerminologyCapabilities_Translation(BackboneElement):
	needsMap: bool

class TerminologyCapabilities_CodeSystem_Version_Filter(BackboneElement):
	code: str
	op: list[str]

class TerminologyCapabilities_CodeSystem_Version(BackboneElement):
	code: Optional[str] = None
	compositional: Optional[bool] = None
	filter: list[TerminologyCapabilities_CodeSystem_Version_Filter] = []
	isDefault: Optional[bool] = None
	language: list[str] = []
	property: list[str] = []

class TerminologyCapabilities_CodeSystem(BackboneElement):
	subsumption: Optional[bool] = None
	uri: Optional[str] = None
	version: list[TerminologyCapabilities_CodeSystem_Version] = []

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
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	expansion: Optional[TerminologyCapabilities_Expansion] = None
	title: Optional[str] = None
	status: str
	validateCode: Optional[TerminologyCapabilities_ValidateCode] = None
	kind: str
	translation: Optional[TerminologyCapabilities_Translation] = None
	url: Optional[str] = None
	codeSystem: list[TerminologyCapabilities_CodeSystem] = []
	software: Optional[TerminologyCapabilities_Software] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	implementation: Optional[TerminologyCapabilities_Implementation] = None
	codeSearch: Optional[str] = None
	lockedDate: Optional[bool] = None
	closure: Optional[TerminologyCapabilities_Closure] = None

