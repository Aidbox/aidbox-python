from pydantic import *
from typing import Optional, List
from ..base import *

class Linkage_Item(BackboneElement):
	type: str
	resource: Reference

class Linkage(DomainResource):
	active: Optional[bool] = None
	author: Optional[Reference] = None
	item: List[Linkage_Item]