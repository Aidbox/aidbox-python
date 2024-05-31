from pydantic import *
from typing import Optional, List
from ..base import *

class ImplementationGuide_Definition_Grouping(BackboneElement):
	name: str
	description: Optional[str] = None

class ImplementationGuide_Definition_Resource(BackboneElement):
	reference: Reference
	fhirVersion: Optional[List[str]] = None
	name: Optional[str] = None
	description: Optional[str] = None
	exampleBoolean: Optional[bool] = None
	exampleCanonical: Optional[str] = None
	groupingId: Optional[str] = None

class ImplementationGuide_Definition_Page(BackboneElement):
	nameUrl: Optional[str] = None
	nameReference: Optional[Reference] = None
	title: str
	generation: str
	page: Optional[List[str]] = None

class ImplementationGuide_Definition_Parameter(BackboneElement):
	code: str
	value: str

class ImplementationGuide_Definition_Template(BackboneElement):
	code: str
	source: str
	scope: Optional[str] = None

class ImplementationGuide_Definition(BackboneElement):
	grouping: Optional[List[ImplementationGuide_Definition_Grouping]] = None
	resource: List[ImplementationGuide_Definition_Resource]
	page: Optional[ImplementationGuide_Definition_Page] = None
	parameter: Optional[List[ImplementationGuide_Definition_Parameter]] = None
	template: Optional[List[ImplementationGuide_Definition_Template]] = None

class ImplementationGuide_Global(BackboneElement):
	type: str
	profile: str

class ImplementationGuide_DependsOn(BackboneElement):
	uri: str
	packageId: Optional[str] = None
	version: Optional[str] = None

class ImplementationGuide_Manifest_Resource(BackboneElement):
	reference: Reference
	exampleBoolean: Optional[bool] = None
	exampleCanonical: Optional[str] = None
	relativePath: Optional[str] = None

class ImplementationGuide_Manifest_Page(BackboneElement):
	name: str
	title: Optional[str] = None
	anchor: Optional[List[str]] = None

class ImplementationGuide_Manifest(BackboneElement):
	rendering: Optional[str] = None
	resource: List[ImplementationGuide_Manifest_Resource]
	page: Optional[List[ImplementationGuide_Manifest_Page]] = None
	image: Optional[List[str]] = None
	other: Optional[List[str]] = None

class ImplementationGuide(DomainResource):
	description: Optional[str] = None
	definition: Optional[ImplementationGuide_Definition] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	fhirVersion: List[str]
	license: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	global_: Optional[List[ImplementationGuide_Global]] = None
	dependsOn: Optional[List[ImplementationGuide_DependsOn]] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	manifest: Optional[ImplementationGuide_Manifest] = None
	title: Optional[str] = None
	status: str
	url: str
	version: Optional[str] = None
	packageId: str
	contact: Optional[List[ContactDetail]] = None