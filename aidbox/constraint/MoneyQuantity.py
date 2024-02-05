from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class MoneyQuantity(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/MoneyQuantity"])
	value: Optional[str] = None
	comparator: Optional[str] = None
	unit: Optional[str] = None
	system: Optional[str] = None
	code: Optional[str] = None