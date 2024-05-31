from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Shareablelibrary(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/shareablelibrary"])
	description: str
	date: Optional[str] = None
	dataRequirement: Optional[List[DataRequirement]] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: str
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	content: Optional[List[Attachment]] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: str
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	type: CodeableConcept
	experimental: bool
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: str
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	reviewer: Optional[List[ContactDetail]] = None
	version: str
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	parameter: Optional[List[ParameterDefinition]] = None
	effectivePeriod: Optional[Period] = None