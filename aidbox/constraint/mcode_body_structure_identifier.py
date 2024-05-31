from pydantic import *
from typing import Optional, List, Literal
from ..base import *
class CodingBodyStructure(Coding):
	system: Literal["http://hl7.org/fhir/resource-types"] = "http://hl7.org/fhir/resource-types"
	code: Literal["BodyStructure"] = "BodyStructure"

class McodeBodyStructureIdentifierType(CodeableConcept):
	coding: List[CodingBodyStructure] = [CodingBodyStructure()]


class McodeBodyStructureIdentifier(Element):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-body-structure-identifier"])
	use: Literal["usual"] = "usual"
	type: Optional[McodeBodyStructureIdentifierType] = None
	system: Optional[str] = None
	value: str
	period: Optional[Period] = None
	assigner: Optional[Reference] = None