from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Practitioner_Qualification(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	code: CodeableConcept
	period: Optional[Period] = None
	issuer: Optional[Reference] = None

class UsCorePractitioner(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"])
	address: Optional[List[Address]] = None
	name: List[HumanName]
	birthDate: Optional[str] = None
	photo: Optional[List[Attachment]] = None
	active: Optional[bool] = None
	communication: Optional[List[CodeableConcept]] = None
	identifier: List[Identifier]
	qualification: Optional[List[Practitioner_Qualification]] = None
	telecom: Optional[List[ContactPoint]] = None
	gender: Optional[str] = None