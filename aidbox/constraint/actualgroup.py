from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Group_Member(BackboneElement):
	entity: Reference
	period: Optional[Period] = None
	inactive: Optional[bool] = None

class Group_Characteristic(BackboneElement):
	exclude: bool
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	valueBoolean: Optional[bool] = None
	code: CodeableConcept
	valueCodeableConcept: Optional[CodeableConcept] = None
	period: Optional[Period] = None
	valueRange: Optional[Range] = None

class Actualgroup(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/actualgroup"])
	name: Optional[str] = None
	type: str
	member: Optional[List[Group_Member]] = None
	active: Optional[bool] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	quantity: Optional[str] = None
	managingEntity: Optional[Reference] = None
	actual: bool
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None