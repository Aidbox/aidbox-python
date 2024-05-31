from pydantic import *
from typing import Optional, List, Literal
from ..base import *

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

class Groupdefinition(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/groupdefinition"])
	name: Optional[str] = None
	type: str
	characteristic: Optional[List[Group_Characteristic]] = None
	active: Optional[bool] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	quantity: Optional[NonNegativeInt] = None
	managingEntity: Optional[Reference] = None
	actual: bool