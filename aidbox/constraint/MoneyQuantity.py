from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class MoneyQuantity(Element):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/MoneyQuantity"])
	value: Optional[float] = None
	comparator: Optional[str] = None
	unit: Optional[str] = None
	system: Optional[str] = None
	code: Optional[str] = None