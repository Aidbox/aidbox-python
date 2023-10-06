from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import UsageContext
from base import Identifier
from base import ContactDetail
from base import BackboneElement
from base import DomainResource


class ExampleScenario(DomainResource):
	date: Optional[str] = None
	publisher: Optional[str] = None
	instance: list[BackboneElement] = []
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	process: list[BackboneElement] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	workflow: list[str] = []
	status: str
	url: Optional[str] = None
	identifier: list[Identifier] = []
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	actor: list[BackboneElement] = []

