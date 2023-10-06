from typing import Optional

from base import Reference
from base import Address
from base import HumanName
from base import CodeableConcept
from base import Attachment
from base import BackboneElement
from base import Identifier
from base import ContactPoint
from base import Period
from base import DomainResource


class RelatedPerson(DomainResource):
	patient: Reference
	address: list[Address] = []
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	relationship: list[CodeableConcept] = []
	photo: list[Attachment] = []
	active: Optional[bool] = None
	communication: list[BackboneElement] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None
	period: Optional[Period] = None

