from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import ContactDetail
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class TerminologyCapabilities(DomainResource):
	description: Optional[str] = None
	date: str
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
	validateCode: Optional[BackboneElement] = None
	kind: str
	translation: Optional[BackboneElement] = None
	url: Optional[str] = None
	codeSystem: list[BackboneElement] = []
	software: Optional[BackboneElement] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	implementation: Optional[BackboneElement] = None
	codeSearch: Optional[str] = None
	lockedDate: Optional[bool] = None
	closure: Optional[BackboneElement] = None

