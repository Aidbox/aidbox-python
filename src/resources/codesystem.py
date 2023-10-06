from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import UsageContext
from base import BackboneElement
from base import Identifier
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


class CodeSystem(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	versionNeeded: Optional[bool] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	content: str
	property: list[BackboneElement] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	filter: list[BackboneElement] = []
	supplements: Optional[str] = None
	compositional: Optional[bool] = None
	status: str
	hierarchyMeaning: Optional[str] = None
	valueSet: Optional[str] = None
	count: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	concept: list[BackboneElement] = []
	caseSensitive: Optional[bool] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

