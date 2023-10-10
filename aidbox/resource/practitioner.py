from typing import Optional
from ..base import *

class Practitioner_Qualification(BackboneElement):
	code: CodeableConcept
	identifier: list[Identifier] = []
	issuer: Optional[Reference] = None
	period: Optional[Period] = None

class Practitioner(DomainResource):
	address: list[Address] = []
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	photo: list[Attachment] = []
	active: Optional[bool] = None
	communication: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	qualification: list[Practitioner_Qualification] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None

