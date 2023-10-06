from typing import Optional

from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import ContactDetail
from base import BackboneElement
from base import DomainResource


class OperationDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	system: bool
	publisher: Optional[str] = None
	instance: bool
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	name: str
	useContext: list[UsageContext] = []
	type: bool
	overload: list[BackboneElement] = []
	experimental: Optional[bool] = None
	outputProfile: Optional[str] = None
	title: Optional[str] = None
	status: str
	resource: list[str] = []
	affectsState: Optional[bool] = None
	kind: str
	comment: Optional[str] = None
	url: Optional[str] = None
	code: str
	base: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	inputProfile: Optional[str] = None
	parameter: list[BackboneElement] = []

