from typing import Optional

from base import BackboneElement
from base import CodeableConcept
from base import BackboneElement
from base import BackboneElement
from base import UsageContext
from base import BackboneElement
from base import ContactDetail
from base import DomainResource


class ImplementationGuide(DomainResource):
	description: Optional[str] = None
	definition: Optional[BackboneElement] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	fhirVersion: list[str]
	license: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	global_: list[BackboneElement] = []
	dependsOn: list[BackboneElement] = []
	name: str
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	manifest: Optional[BackboneElement] = None
	title: Optional[str] = None
	status: str
	url: str
	version: Optional[str] = None
	packageId: str
	contact: list[ContactDetail] = []

