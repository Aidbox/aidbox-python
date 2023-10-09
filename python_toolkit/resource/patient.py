from typing import Optional
from ..base import *

class Patient_Link(BackboneElement):
	other: Reference
	type: str

class Patient_Communication(BackboneElement):
	language: CodeableConcept
	preferred: Optional[bool] = None

class Patient_Contact(BackboneElement):
	address: Optional[Address] = None
	gender: Optional[str] = None
	name: Optional[HumanName] = None
	organization: Optional[Reference] = None
	period: Optional[Period] = None
	relationship: list[CodeableConcept] = []
	telecom: list[ContactPoint] = []

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
	link: list[Patient_Link] = []
	active: Optional[bool] = None
	communication: list[Patient_Communication] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	generalPractitioner: list[Reference] = []
	gender: Optional[str] = None
	maritalStatus: Optional[CodeableConcept] = None
	contact: list[Patient_Contact] = []

