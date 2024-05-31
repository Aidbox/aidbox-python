from pydantic import *
from typing import Optional, List
from ..base import *

class Organization_Contact(BackboneElement):
	purpose: Optional[CodeableConcept] = None
	name: Optional[HumanName] = None
	telecom: Optional[List[ContactPoint]] = None
	address: Optional[Address] = None

class Organization(DomainResource):
	address: Optional[List[Address]] = None
	name: Optional[str] = None
	type: Optional[List[CodeableConcept]] = None
	alias: Optional[List[str]] = None
	active: Optional[bool] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	partOf: Optional[Reference] = None
	endpoint: Optional[List[Reference]] = None
	contact: Optional[List[Organization_Contact]] = None