from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Cqllibrary(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/cqllibrary"])
	description: Optional[str] = None
	date: Optional[str] = None
	dataRequirement: Optional[List[DataRequirement]] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	content: Optional[List[Attachment]] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	type: CodeableConcept
	experimental: Optional[bool] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	reviewer: Optional[List[ContactDetail]] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	parameter: Optional[List[ParameterDefinition]] = None
	effectivePeriod: Optional[Period] = None