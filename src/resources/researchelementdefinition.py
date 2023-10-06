from typing import Optional

from base import ContactDetail
from base import CodeableConcept
from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import ContactDetail
from base import BackboneElement
from base import Identifier
from base import ContactDetail
from base import ContactDetail
from base import RelatedArtifact
from base import ContactDetail
from base import Reference
from base import Period
from base import DomainResource


class ResearchElementDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	variableType: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	characteristic: list[BackboneElement]
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	comment: list[str] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None

