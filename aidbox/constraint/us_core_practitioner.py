from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Practitioner_Qualification(BackboneElement):
	identifier: Optional[List[Identifier]] = None
	code: CodeableConcept
	period: Optional[Period] = None
	issuer: Optional[Reference] = None

class UsCorePractitioner(BaseModel):
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
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None