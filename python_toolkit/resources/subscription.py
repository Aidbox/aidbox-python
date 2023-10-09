from typing import Optional
from base import *

class Subscription_Channel(BackboneElement):
	endpoint: Optional[str] = None
	header: list[str] = []
	payload: Optional[str] = None
	type: str

class Subscription(DomainResource):
	channel: Subscription_Channel
	contact: list[ContactPoint] = []
	criteria: str
	end: Optional[str] = None
	error: Optional[str] = None
	reason: str
	status: str

