from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class SimpleQuantity(Element):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/SimpleQuantity"])
	value: Optional[float] = None
	unit: Optional[str] = None
	system: Optional[str] = None
	code: Optional[str] = None