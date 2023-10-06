from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import UsageContext
from base import Identifier
from base import ContactDetail
from base import DomainResource


class ConceptMap(DomainResource):
	description: Optional[str] = None
	sourceCanonical: Optional[str] = None
	date: Optional[str] = None
	targetUri: Optional[str] = None
	group: list[BackboneElement] = []
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	targetCanonical: Optional[str] = None
	status: str
	sourceUri: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[Identifier] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []

