from typing import Optional

from base import BackboneElement
from base import Reference
from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import Identifier
from base import ContactDetail
from base import BackboneElement
from base import Period
from base import DomainResource


class ChargeItemDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	propertyGroup: list[BackboneElement] = []
	instance: list[Reference] = []
	jurisdiction: list[CodeableConcept] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	derivedFromUri: list[str] = []
	status: str
	url: str
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	replaces: list[str] = []
	partOf: list[str] = []
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	applicability: list[BackboneElement] = []
	effectivePeriod: Optional[Period] = None

