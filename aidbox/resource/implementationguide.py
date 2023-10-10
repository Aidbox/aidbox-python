from typing import Optional
from ..base import *

class ImplementationGuide_Definition_Grouping(BackboneElement):
	description: Optional[str] = None
	name: str

class ImplementationGuide_Definition_Page(BackboneElement):
	generation: str
	nameReference: Optional[Reference] = None
	nameUrl: Optional[str] = None
	page: list[str] = []
	title: str

class ImplementationGuide_Definition_Parameter(BackboneElement):
	code: str
	value: str

class ImplementationGuide_Definition_Resource(BackboneElement):
	description: Optional[str] = None
	exampleBoolean: Optional[bool] = None
	exampleCanonical: Optional[str] = None
	fhirVersion: list[str] = []
	groupingId: Optional[str] = None
	name: Optional[str] = None
	reference: Reference

class ImplementationGuide_Definition_Template(BackboneElement):
	code: str
	scope: Optional[str] = None
	source: str

class ImplementationGuide_Definition(BackboneElement):
	grouping: list[ImplementationGuide_Definition_Grouping] = []
	page: Optional[ImplementationGuide_Definition_Page] = None
	parameter: list[ImplementationGuide_Definition_Parameter] = []
	resource: list[ImplementationGuide_Definition_Resource]
	template: list[ImplementationGuide_Definition_Template] = []

class ImplementationGuide_Global(BackboneElement):
	profile: str
	type: str

class ImplementationGuide_DependsOn(BackboneElement):
	packageId: Optional[str] = None
	uri: str
	version: Optional[str] = None

class ImplementationGuide_Manifest_Page(BackboneElement):
	anchor: list[str] = []
	name: str
	title: Optional[str] = None

class ImplementationGuide_Manifest_Resource(BackboneElement):
	exampleBoolean: Optional[bool] = None
	exampleCanonical: Optional[str] = None
	reference: Reference
	relativePath: Optional[str] = None

class ImplementationGuide_Manifest(BackboneElement):
	image: list[str] = []
	other: list[str] = []
	page: list[ImplementationGuide_Manifest_Page] = []
	rendering: Optional[str] = None
	resource: list[ImplementationGuide_Manifest_Resource]

class ImplementationGuide(DomainResource):
	description: Optional[str] = None
	definition: Optional[ImplementationGuide_Definition] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	fhirVersion: list[str]
	license: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	global_: list[ImplementationGuide_Global] = []
	dependsOn: list[ImplementationGuide_DependsOn] = []
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	manifest: Optional[ImplementationGuide_Manifest] = None
	title: Optional[str] = None
	status: str
	url: str
	version: Optional[str] = None
	packageId: str
	contact: list[ContactDetail] = []

