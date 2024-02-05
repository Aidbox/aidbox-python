from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class CodingC19700(Coding):
	system: Literal["http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"] = "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl"
	code: Literal["C19700"] = "C19700"

class McodePatientGroupCode(CodeableConcept):
	coding: List[CodingC19700] = [CodingC19700()]


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

class McodePatientGroup(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-patient-group"])
	name: Optional[str] = None
	type: str
	member: Optional[List[Group_Member]] = None
	characteristic: Optional[List[Group_Characteristic]] = None
	active: Optional[bool] = None
	code: Optional[McodePatientGroupCode] = None
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