from typing import Optional

from base import BackboneElement
from base import ContactPoint
from base import DomainResource


class Subscription(DomainResource):
	channel: BackboneElement
	contact: list[ContactPoint] = []
	criteria: str
	end: Optional[str] = None
	error: Optional[str] = None
	reason: str
	status: str

