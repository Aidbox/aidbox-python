from typing import Optional
from base import *

class Evidence(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	outcome: list[Reference] = []
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	note: list[Annotation] = []
	author: list[ContactDetail] = []
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	exposureBackground: Reference
	effectivePeriod: Optional[Period] = None
	exposureVariant: list[Reference] = []

