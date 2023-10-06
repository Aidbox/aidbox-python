from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import BackboneElement
from base import BackboneElement
from base import ContactDetail
from base import BackboneElement
from base import BackboneElement
from base import DomainResource


class CapabilityStatement(DomainResource):
	description: Optional[str] = None
	format: list[str]
	date: str
	publisher: Optional[str] = None
	patchFormat: list[str] = []
	fhirVersion: str
	jurisdiction: list[CodeableConcept] = []
	instantiates: list[str] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	imports: list[str] = []
	title: Optional[str] = None
	document: list[BackboneElement] = []
	status: str
	messaging: list[BackboneElement] = []
	kind: str
	implementationGuide: list[str] = []
	url: Optional[str] = None
	software: Optional[BackboneElement] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	implementation: Optional[BackboneElement] = None
	rest: list[BackboneElement] = []

