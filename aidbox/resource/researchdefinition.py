from pydantic import *
from typing import Optional, List
from ..base import *

class ResearchDefinition(DomainResource):
	description: Optional[str] = None
	exposureAlternative: Optional[Reference] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	outcome: Optional[Reference] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	population: Reference
	comment: Optional[List[str]] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	reviewer: Optional[List[ContactDetail]] = None
	shortTitle: Optional[str] = None
	exposure: Optional[Reference] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None