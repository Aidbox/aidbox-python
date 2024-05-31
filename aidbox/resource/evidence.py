from pydantic import *
from typing import Optional, List
from ..base import *

class Evidence(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	outcome: Optional[List[Reference]] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	author: Optional[List[ContactDetail]] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	reviewer: Optional[List[ContactDetail]] = None
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	exposureBackground: Reference
	effectivePeriod: Optional[Period] = None
	exposureVariant: Optional[List[Reference]] = None