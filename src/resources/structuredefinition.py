from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import UsageContext
from base import BackboneElement
from base import Coding
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


class StructureDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	derivation: Optional[str] = None
	publisher: Optional[str] = None
	contextInvariant: list[str] = []
	fhirVersion: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	mapping: list[BackboneElement] = []
	useContext: list[UsageContext] = []
	abstract: bool
	copyright: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	title: Optional[str] = None
	snapshot: Optional[BackboneElement] = None
	keyword: list[Coding] = []
	status: str
	kind: str
	url: str
	identifier: list[Identifier] = []
	context: list[BackboneElement] = []
	version: Optional[str] = None
	differential: Optional[BackboneElement] = None
	contact: list[ContactDetail] = []
	baseDefinition: Optional[str] = None

