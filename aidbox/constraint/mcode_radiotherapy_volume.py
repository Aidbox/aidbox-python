from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class McodeRadiotherapyVolume(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-radiotherapy-volume"])
	identifier: Optional[List[Identifier]] = None
	active: Optional[bool] = None
	morphology: Optional[CodeableConcept] = None
	location: Optional[CodeableConcept] = None
	locationQualifier: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None
	image: Optional[List[Attachment]] = None
	patient: Reference
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None