from pydantic import *
from typing import Optional, List
from ..base import *

class RelatedPerson_Communication(BackboneElement):
	language: CodeableConcept
	preferred: Optional[bool] = None

class RelatedPerson(DomainResource):
	patient: Reference
	address: Optional[List[Address]] = None
	name: Optional[List[HumanName]] = None
	birthDate: Optional[str] = None
	relationship: Optional[List[CodeableConcept]] = None
	photo: Optional[List[Attachment]] = None
	active: Optional[bool] = None
	communication: Optional[List[RelatedPerson_Communication]] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	gender: Optional[str] = None
	period: Optional[Period] = None