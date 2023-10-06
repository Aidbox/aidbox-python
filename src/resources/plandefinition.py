from typing import Optional

from base import ContactDetail
from base import CodeableConcept
from base import CodeableConcept
from base import UsageContext
from base import BackboneElement
from base import CodeableConcept
from base import CodeableConcept
from base import ContactDetail
from base import Identifier
from base import ContactDetail
from base import BackboneElement
from base import ContactDetail
from base import RelatedArtifact
from base import ContactDetail
from base import Reference
from base import Period
from base import DomainResource


class PlanDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	goal: list[BackboneElement] = []
	copyright: Optional[str] = None
	type: Optional[CodeableConcept] = None
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	action: list[BackboneElement] = []
	reviewer: list[ContactDetail] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None

