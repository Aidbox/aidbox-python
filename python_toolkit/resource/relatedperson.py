from typing import Optional
from ..base import *

class RelatedPerson_Communication(BackboneElement):
	language: CodeableConcept
	preferred: Optional[bool] = None

class RelatedPerson(DomainResource):
	patient: Reference
	address: list[Address] = []
	name: list[HumanName] = []
	birthDate: Optional[str] = None
	relationship: list[CodeableConcept] = []
	photo: list[Attachment] = []
	active: Optional[bool] = None
	communication: list[RelatedPerson_Communication] = []
	identifier: list[Identifier] = []
	telecom: list[ContactPoint] = []
	gender: Optional[str] = None
	period: Optional[Period] = None

