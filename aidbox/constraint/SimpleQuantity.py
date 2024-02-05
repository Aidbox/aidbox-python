from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class SimpleQuantity(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/SimpleQuantity"])
	value: Optional[str] = None
	unit: Optional[str] = None
	system: Optional[str] = None
	code: Optional[str] = None