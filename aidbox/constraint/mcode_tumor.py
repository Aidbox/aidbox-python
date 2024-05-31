from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class Coding367651003(Coding):
	display: Literal["Malignant neoplasm of primary, secondary, or uncertain origin (morphologic abnormality)"] = "Malignant neoplasm of primary, secondary, or uncertain origin (morphologic abnormality)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["367651003"] = "367651003"

class McodeTumorMorphology(CodeableConcept):
	coding: List[Coding367651003] = [Coding367651003()]


class McodeTumor(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-tumor"])
	identifier: List[Identifier]
	active: Optional[bool] = None
	morphology: Optional[McodeTumorMorphology] = None
	location: CodeableConcept
	locationQualifier: Optional[List[CodeableConcept]] = None
	description: Optional[str] = None
	image: Optional[List[Attachment]] = None
	patient: Reference