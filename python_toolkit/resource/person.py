from typing import Optional
from ..base import *

class Person_Link(BackboneElement):
	assurance: Optional[str] = None
	target: Reference

class Person(DomainResource):
	address: list[Address] = []
	managingOrganization: Optional[Reference] = None
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	photo: Optional[Attachment] = None
	link: list[Person_Link] = []
	active: Optional[bool] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None

