from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class CodexrtRadiotherapyVolume(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-volume"])
	identifier: Optional[List[Identifier]] = None
	active: Optional[bool] = None
	morphology: Optional[CodeableConcept] = None
	location: Optional[CodeableConcept] = None
	locationQualifier: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None
	image: Optional[List[Attachment]] = None
	patient: Reference