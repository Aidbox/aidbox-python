from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import Identifier
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import ContactDetail
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import Reference
from base import DomainResource


class TestScript(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	variable: list[BackboneElement] = []
	publisher: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	setup: Optional[BackboneElement] = None
	status: str
	url: str
	identifier: Optional[Identifier] = None
	origin: list[BackboneElement] = []
	fixture: list[BackboneElement] = []
	version: Optional[str] = None
	teardown: Optional[BackboneElement] = None
	contact: list[ContactDetail] = []
	metadata: Optional[BackboneElement] = None
	destination: list[BackboneElement] = []
	test: list[BackboneElement] = []
	profile: list[Reference] = []

