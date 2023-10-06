from typing import Optional

from base import CodeableConcept
from base import BackboneElement
from base import UsageContext
from base import Coding
from base import Identifier
from base import ContactDetail
from base import Period
from base import DomainResource


class Questionnaire(DomainResource):
	description: Optional[str] = None
	subjectType: list[str] = []
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	derivedFrom: list[str] = []
	purpose: Optional[str] = None
	name: Optional[str] = None
	item: list[BackboneElement] = []
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	code: list[Coding] = []
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	version: Optional[str] = None
	contact: list[ContactDetail] = []
	effectivePeriod: Optional[Period] = None

