from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Organization_Contact(BackboneElement):
	purpose: Optional[CodeableConcept] = None
	name: Optional[HumanName] = None
	telecom: Optional[List[ContactPoint]] = None
	address: Optional[Address] = None

class UsCoreOrganization(DomainResource):
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