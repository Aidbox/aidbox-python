from typing import Optional

from base import Address
from base import Reference
from base import HumanName
from base import Attachment
from base import BackboneElement
from base import BackboneElement
from base import Identifier
from base import ContactPoint
from base import Reference
from base import CodeableConcept
from base import BackboneElement
from base import DomainResource


class Patient(DomainResource):
	multipleBirthBoolean: Optional[bool] = None
	address: list[Address] = []
	deceasedDateTime: Optional[str] = None
	managingOrganization: Optional[Reference] = None
	deceasedBoolean: Optional[bool] = None
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	multipleBirthInteger: Optional[int] = None
	photo: list[Attachment] = []
	link: list[BackboneElement] = []
	active: Optional[bool] = None
	communication: list[BackboneElement] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	generalPractitioner: list[Reference] = []
	gender: Optional[str] = None
	maritalStatus: Optional[CodeableConcept] = None
	contact: list[BackboneElement] = []

