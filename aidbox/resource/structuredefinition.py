from typing import Optional
from ..base import *

class StructureDefinition_Mapping(BackboneElement):
	comment: Optional[str] = None
	identity: str
	name: Optional[str] = None
	uri: Optional[str] = None

class StructureDefinition_Snapshot(BackboneElement):
	element: list[ElementDefinition]

class StructureDefinition_Context(BackboneElement):
	expression: str
	type: str

class StructureDefinition_Differential(BackboneElement):
	element: list[ElementDefinition]

class StructureDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	derivation: Optional[str] = None
	publisher: Optional[str] = None
	contextInvariant: list[str] = []
	fhirVersion: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	mapping: list[StructureDefinition_Mapping] = []
	useContext: list[UsageContext] = []
	abstract: bool
	copyright: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	title: Optional[str] = None
	snapshot: Optional[StructureDefinition_Snapshot] = None
	keyword: list[Coding] = []
	status: str
	kind: str
	url: str
	identifier: list[Identifier] = []
	context: list[StructureDefinition_Context] = []
	version: Optional[str] = None
	differential: Optional[StructureDefinition_Differential] = None
	contact: list[ContactDetail] = []
	baseDefinition: Optional[str] = None

