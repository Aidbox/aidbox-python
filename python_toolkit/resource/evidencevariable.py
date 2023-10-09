from typing import Optional
from ..base import *

class EvidenceVariable_Characteristic(BackboneElement):
	description: Optional[str] = None
	exclude: Optional[bool] = None
	groupMeasure: Optional[str] = None
	definitionExpression: Optional[Expression] = None
	timeFromStart: Optional[str] = None
	participantEffectiveDuration: Optional[str] = None
	definitionDataRequirement: Optional[DataRequirement] = None
	definitionTriggerDefinition: Optional[TriggerDefinition] = None
	definitionCanonical: Optional[str] = None
	definitionReference: Optional[Reference] = None
	participantEffectiveTiming: Optional[str] = None
	participantEffectiveDateTime: Optional[str] = None
	participantEffectivePeriod: Optional[Period] = None
	definitionCodeableConcept: Optional[CodeableConcept] = None
	usageContext: list[UsageContext] = []

class EvidenceVariable(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	type: Optional[str] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	note: list[Annotation] = []
	author: list[ContactDetail] = []
	characteristic: list[EvidenceVariable_Characteristic]
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
	effectivePeriod: Optional[Period] = None

