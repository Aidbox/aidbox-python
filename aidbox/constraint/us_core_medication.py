from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Medication_Ingredient(BackboneElement):
	itemCodeableConcept: Optional[CodeableConcept] = None
	itemReference: Optional[Reference] = None
	isActive: Optional[bool] = None
	strength: Optional[Ratio] = None

class Medication_Batch(BackboneElement):
	lotNumber: Optional[str] = None
	expirationDate: Optional[str] = None

class UsCoreMedication(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-medication"])
	identifier: Optional[List[Identifier]] = None
	code: CodeableConcept
	status: Optional[str] = None
	manufacturer: Optional[Reference] = None
	form: Optional[CodeableConcept] = None
	amount: Optional[Ratio] = None
	ingredient: Optional[List[Medication_Ingredient]] = None
	batch: Optional[Medication_Batch] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None