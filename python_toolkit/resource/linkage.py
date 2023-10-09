from typing import Optional
from base import *

class Linkage_Item(BackboneElement):
	resource: Reference
	type: str

class Linkage(DomainResource):
	active: Optional[bool] = None
	author: Optional[Reference] = None
	item: list[Linkage_Item]

