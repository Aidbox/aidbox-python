from typing import Optional
from base import *

class Organization_Contact(BackboneElement):
	address: Optional[Address] = None
	name: Optional[HumanName] = None
	purpose: Optional[CodeableConcept] = None
	telecom: list[ContactPoint] = []

class Organization(DomainResource):
	address: list[Address] = []
	name: Optional[str] = None
	type: list[CodeableConcept] = []
	alias: list[str] = []
	active: Optional[bool] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	partOf: Optional[Reference] = None
	endpoint: list[Reference] = []
	contact: list[Organization_Contact] = []

