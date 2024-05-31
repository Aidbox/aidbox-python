from pydantic import *
from typing import Optional, List
from ..base import *

class Patient_Link(BackboneElement):
	other: Reference
	type: str

class Patient_Communication(BackboneElement):
	language: CodeableConcept
	preferred: Optional[bool] = None

class Patient_Contact(BackboneElement):
	relationship: Optional[List[CodeableConcept]] = None
	name: Optional[HumanName] = None
	telecom: Optional[List[ContactPoint]] = None
	address: Optional[Address] = None
	gender: Optional[str] = None
	organization: Optional[Reference] = None
	period: Optional[Period] = None

class Patient(DomainResource):
	multipleBirthBoolean: Optional[bool] = None
	address: Optional[List[Address]] = None
	deceasedDateTime: Optional[str] = None
	managingOrganization: Optional[Reference] = None
	deceasedBoolean: Optional[bool] = None
	name: Optional[List[HumanName]] = None
	birthDate: Optional[str] = None
	multipleBirthInteger: Optional[int] = None
	photo: Optional[List[Attachment]] = None
	link: Optional[List[Patient_Link]] = None
	active: Optional[bool] = None
	communication: Optional[List[Patient_Communication]] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	generalPractitioner: Optional[List[Reference]] = None
	gender: Optional[str] = None
	maritalStatus: Optional[CodeableConcept] = None
	contact: Optional[List[Patient_Contact]] = None