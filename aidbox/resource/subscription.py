from pydantic import *
from typing import Optional, List
from ..base import *

class Subscription_Channel(BackboneElement):
	type: str
	endpoint: Optional[str] = None
	payload: Optional[str] = None
	header: Optional[List[str]] = None

class Subscription(DomainResource):
	status: str
	contact: Optional[List[ContactPoint]] = None
	end: Optional[str] = None
	reason: str
	criteria: str
	error: Optional[str] = None
	channel: Subscription_Channel