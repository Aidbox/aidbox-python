from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import Identifier
from base import BackboneElement
from base import ContactDetail
from base import Coding
from base import DomainResource


class MessageDefinition(DomainResource):
	description: Optional[str] = None
	category: Optional[str] = None
	date: str
	publisher: Optional[str] = None
	parent: list[str] = []
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	allowedResponse: list[BackboneElement] = []
	graph: list[str] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	focus: list[BackboneElement] = []
	replaces: list[str] = []
	responseRequired: Optional[str] = None
	base: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	eventUri: Optional[str] = None
	eventCoding: Optional[Coding] = None

