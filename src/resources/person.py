from typing import Optional

from base import Address
from base import Reference
from base import HumanName
from base import Attachment
from base import BackboneElement
from base import Identifier
from base import ContactPoint
from base import DomainResource


class Person(DomainResource):
	address: list[Address] = []
	managingOrganization: Optional[Reference] = None
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	photo: Optional[Attachment] = None
	link: list[BackboneElement] = []
	active: Optional[bool] = None
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None

