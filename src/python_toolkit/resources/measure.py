from typing import Optional

from base import BackboneElement
from base import ContactDetail
from base import CodeableConcept
from base import CodeableConcept
from base import CodeableConcept
from base import UsageContext
from base import CodeableConcept
from base import CodeableConcept
from base import BackboneElement
from base import ContactDetail
from base import Identifier
from base import ContactDetail
from base import CodeableConcept
from base import ContactDetail
from base import RelatedArtifact
from base import ContactDetail
from base import Reference
from base import CodeableConcept
from base import Period
from base import DomainResource


class Measure(DomainResource):
	description: Optional[str] = None
	definition: list[str] = []
	date: Optional[str] = None
	group: list[BackboneElement] = []
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	compositeScoring: Optional[CodeableConcept] = None
	disclaimer: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	guidance: Optional[str] = None
	type: list[CodeableConcept] = []
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	supplementalData: list[BackboneElement] = []
	library: list[str] = []
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	rationale: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	riskAdjustment: Optional[str] = None
	scoring: Optional[CodeableConcept] = None
	reviewer: list[ContactDetail] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	improvementNotation: Optional[CodeableConcept] = None
	rateAggregation: Optional[str] = None
	effectivePeriod: Optional[Period] = None
	clinicalRecommendationStatement: Optional[str] = None

