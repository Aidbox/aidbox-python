from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


class GraphDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	start: str
	useContext: list[UsageContext] = []
	experimental: Optional[bool] = None
	status: str
	link: list[BackboneElement] = []
	url: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	profile: Optional[str] = None

