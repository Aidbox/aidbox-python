from typing import Optional

from base import Address
from base import HumanName
from base import Attachment
from base import CodeableConcept
from base import Identifier
from base import BackboneElement
from base import ContactPoint
from base import DomainResource


class Practitioner(DomainResource):
	address: list[Address] = []
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	photo: list[Attachment] = []
	active: Optional[bool] = None
	communication: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	qualification: list[BackboneElement] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None

