from typing import Optional

from base import Reference
from base import ContactDetail
from base import CodeableConcept
from base import CodeableConcept
from base import UsageContext
from base import Reference
from base import CodeableConcept
from base import ContactDetail
from base import Reference
from base import Identifier
from base import ContactDetail
from base import ContactDetail
from base import Reference
from base import RelatedArtifact
from base import ContactDetail
from base import Reference
from base import Period
from base import DomainResource


class ResearchDefinition(DomainResource):
	description: Optional[str] = None
	exposureAlternative: Optional[Reference] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	outcome: Optional[Reference] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	population: Reference
	comment: list[str] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	shortTitle: Optional[str] = None
	exposure: Optional[Reference] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None

