from pydantic import *
from typing import Optional, List
from ..base import *

class ConceptMap_Group_Element_Target_DependsOn(BackboneElement):
	property: str
	system: Optional[str] = None
	value: str
	display: Optional[str] = None

class ConceptMap_Group_Element_Target(BackboneElement):
	code: Optional[str] = None
	display: Optional[str] = None
	equivalence: str
	comment: Optional[str] = None
	dependsOn: Optional[List[ConceptMap_Group_Element_Target_DependsOn]] = None
	product: Optional[List[str]] = None

class ConceptMap_Group_Element(BackboneElement):
	code: Optional[str] = None
	display: Optional[str] = None
	target: Optional[List[ConceptMap_Group_Element_Target]] = None

class ConceptMap_Group_Unmapped(BackboneElement):
	mode: str
	code: Optional[str] = None
	display: Optional[str] = None
	url: Optional[str] = None

class ConceptMap_Group(BackboneElement):
	source: Optional[str] = None
	sourceVersion: Optional[str] = None
	target: Optional[str] = None
	targetVersion: Optional[str] = None
	element: List[ConceptMap_Group_Element]
	unmapped: Optional[ConceptMap_Group_Unmapped] = None

class ConceptMap(DomainResource):
	description: Optional[str] = None
	sourceCanonical: Optional[str] = None
	date: Optional[str] = None
	targetUri: Optional[str] = None
	group: Optional[List[ConceptMap_Group]] = None
	publisher: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	targetCanonical: Optional[str] = None
	status: str
	sourceUri: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[Identifier] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None