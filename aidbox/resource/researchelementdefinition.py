from pydantic import *
from typing import Optional, List
from ..base import *

class ResearchElementDefinition_Characteristic(BackboneElement):
	studyEffectiveTiming: Optional[Timing] = None
	exclude: Optional[bool] = None
	definitionExpression: Optional[Expression] = None
	participantEffectiveDuration: Optional[Duration] = None
	studyEffectiveDuration: Optional[Duration] = None
	definitionDataRequirement: Optional[DataRequirement] = None
	definitionCanonical: Optional[str] = None
	studyEffectiveGroupMeasure: Optional[str] = None
	participantEffectiveTiming: Optional[Timing] = None
	participantEffectiveGroupMeasure: Optional[str] = None
	studyEffectiveDescription: Optional[str] = None
	participantEffectiveDateTime: Optional[str] = None
	studyEffectiveTimeFromStart: Optional[Duration] = None
	unitOfMeasure: Optional[CodeableConcept] = None
	participantEffectivePeriod: Optional[Period] = None
	participantEffectiveDescription: Optional[str] = None
	definitionCodeableConcept: Optional[CodeableConcept] = None
	usageContext: Optional[List[UsageContext]] = None
	studyEffectivePeriod: Optional[Period] = None
	participantEffectiveTimeFromStart: Optional[Duration] = None
	studyEffectiveDateTime: Optional[str] = None

class ResearchElementDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	variableType: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	characteristic: List[ResearchElementDefinition_Characteristic]
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	comment: Optional[List[str]] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	reviewer: Optional[List[ContactDetail]] = None
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None