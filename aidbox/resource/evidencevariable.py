from pydantic import *
from typing import Optional, List
from ..base import *

class EvidenceVariable_Characteristic(BackboneElement):
	description: Optional[str] = None
	exclude: Optional[bool] = None
	groupMeasure: Optional[str] = None
	definitionExpression: Optional[Expression] = None
	timeFromStart: Optional[Duration] = None
	participantEffectiveDuration: Optional[Duration] = None
	definitionDataRequirement: Optional[DataRequirement] = None
	definitionTriggerDefinition: Optional[TriggerDefinition] = None
	definitionCanonical: Optional[str] = None
	definitionReference: Optional[Reference] = None
	participantEffectiveTiming: Optional[Timing] = None
	participantEffectiveDateTime: Optional[str] = None
	participantEffectivePeriod: Optional[Period] = None
	definitionCodeableConcept: Optional[CodeableConcept] = None
	usageContext: Optional[List[UsageContext]] = None

class EvidenceVariable(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	type: Optional[str] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	author: Optional[List[ContactDetail]] = None
	characteristic: List[EvidenceVariable_Characteristic]
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
	effectivePeriod: Optional[Period] = None