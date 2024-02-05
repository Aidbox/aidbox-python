from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Organization_Contact(BackboneElement):
	purpose: Optional[CodeableConcept] = None
	name: Optional[HumanName] = None
	telecom: Optional[List[ContactPoint]] = None
	address: Optional[Address] = None

class UsCoreOrganization(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"])
	address: Optional[List[Address]] = None
	name: str
	type: Optional[List[CodeableConcept]] = None
	alias: Optional[List[str]] = None
	active: bool
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	partOf: Optional[Reference] = None
	endpoint: Optional[List[Reference]] = None
	contact: Optional[List[Organization_Contact]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None