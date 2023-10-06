from typing import Optional

from base import UsageContext
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


class CompartmentDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	experimental: Optional[bool] = None
	search: bool
	status: str
	resource: list[BackboneElement] = []
	url: str
	code: str
	version: Optional[str] = None
	contact: list[ContactDetail] = []

