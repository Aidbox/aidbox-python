from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import Identifier
from base import ContactDetail
from base import DomainResource


class ValueSet(DomainResource):
	description: Optional[str] = None
	compose: Optional[BackboneElement] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	expansion: Optional[BackboneElement] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	identifier: list[Identifier] = []
	immutable: Optional[bool] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

