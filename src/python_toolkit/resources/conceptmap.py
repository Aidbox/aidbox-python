from typing import Optional
from base import *

class ConceptMap_Group_Element_Target_DependsOn(BackboneElement):
	display: Optional[str] = None
	property: str
	system: Optional[str] = None
	value: str

class ConceptMap_Group_Element_Target(BackboneElement):
	code: Optional[str] = None
	comment: Optional[str] = None
	dependsOn: list[ConceptMap_Group_Element_Target_DependsOn] = []
	display: Optional[str] = None
	equivalence: str
	product: list[str] = []

class ConceptMap_Group_Element(BackboneElement):
	code: Optional[str] = None
	display: Optional[str] = None
	target: list[ConceptMap_Group_Element_Target] = []

class ConceptMap_Group_Unmapped(BackboneElement):
	code: Optional[str] = None
	display: Optional[str] = None
	mode: str
	url: Optional[str] = None

class ConceptMap_Group(BackboneElement):
	element: list[ConceptMap_Group_Element]
	source: Optional[str] = None
	sourceVersion: Optional[str] = None
	target: Optional[str] = None
	targetVersion: Optional[str] = None
	unmapped: Optional[ConceptMap_Group_Unmapped] = None

class ConceptMap(DomainResource):
	description: Optional[str] = None
	sourceCanonical: Optional[str] = None
	date: Optional[str] = None
	targetUri: Optional[str] = None
	group: list[ConceptMap_Group] = []
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	targetCanonical: Optional[str] = None
	status: str
	sourceUri: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[Identifier] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

