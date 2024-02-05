from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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

class McodeCancerPatient(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-cancer-patient"])
	multipleBirthBoolean: Optional[bool] = None
	address: Optional[List[Address]] = None
	deceasedDateTime: Optional[str] = None
	managingOrganization: Optional[Reference] = None
	deceasedBoolean: Optional[bool] = None
	name: List[HumanName]
	birthDate: Optional[str] = None
	multipleBirthInteger: Optional[int] = None
	photo: Optional[List[Attachment]] = None
	link: Optional[List[Patient_Link]] = None
	active: Optional[bool] = None
	communication: Optional[List[Patient_Communication]] = None
	identifier: List[Identifier]
	telecom: Optional[List[ContactPoint]] = None
	generalPractitioner: Optional[List[Reference]] = None
	gender: str
	maritalStatus: Optional[CodeableConcept] = None
	contact: Optional[List[Patient_Contact]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None