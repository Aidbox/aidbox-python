from typing import Optional
from ..base import *

class Group_Member(BackboneElement):
	entity: Reference
	inactive: Optional[bool] = None
	period: Optional[Period] = None

class Group_Characteristic(BackboneElement):
	exclude: bool
	valueReference: Optional[Reference] = None
	valueQuantity: Optional[Quantity] = None
	valueBoolean: Optional[bool] = None
	code: CodeableConcept
	valueCodeableConcept: Optional[CodeableConcept] = None
	period: Optional[Period] = None
	valueRange: Optional[Range] = None

class Group(DomainResource):
	name: Optional[str] = None
	type: str
	member: list[Group_Member] = []
	characteristic: list[Group_Characteristic] = []
	active: Optional[bool] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	quantity: Optional[str] = None
	managingEntity: Optional[Reference] = None
	actual: bool

