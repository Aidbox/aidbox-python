from typing import Optional

from base import Reference
from base import BackboneElement
from base import DomainResource


class Linkage(DomainResource):
	active: Optional[bool] = None
	author: Optional[Reference] = None
	item: list[BackboneElement]

