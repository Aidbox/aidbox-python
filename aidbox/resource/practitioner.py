from pydantic import *
from typing import Optional, List
from ..base import *

class Practitioner_Qualification(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	code: CodeableConcept
	period: Optional[Period] = None
	issuer: Optional[Reference] = None

class Practitioner(DomainResource):
	address: Optional[List[Address]] = None
	name: Optional[List[HumanName]] = None
	birthDate: Optional[str] = None
	photo: Optional[List[Attachment]] = None
	active: Optional[bool] = None
	communication: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	qualification: Optional[List[Practitioner_Qualification]] = None
	telecom: Optional[List[ContactPoint]] = None
	gender: Optional[str] = None