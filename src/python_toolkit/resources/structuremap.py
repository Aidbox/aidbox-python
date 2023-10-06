from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import Identifier
from base import ContactDetail
from base import DomainResource


class StructureMap(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	group: list[BackboneElement]
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	structure: list[BackboneElement] = []
	status: str
	url: str
	identifier: list[Identifier] = []
	version: Optional[str] = None
	import_: list[str] = []
	contact: list[ContactDetail] = []

