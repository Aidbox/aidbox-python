from typing import Optional
from ..base import *

class ResearchElementDefinition_Characteristic(BackboneElement):
	studyEffectiveTiming: Optional[str] = None
	exclude: Optional[bool] = None
	definitionExpression: Optional[Expression] = None
	participantEffectiveDuration: Optional[str] = None
	studyEffectiveDuration: Optional[str] = None
	definitionDataRequirement: Optional[DataRequirement] = None
	definitionCanonical: Optional[str] = None
	studyEffectiveGroupMeasure: Optional[str] = None
	participantEffectiveTiming: Optional[str] = None
	participantEffectiveGroupMeasure: Optional[str] = None
	studyEffectiveDescription: Optional[str] = None
	participantEffectiveDateTime: Optional[str] = None
	studyEffectiveTimeFromStart: Optional[str] = None
	unitOfMeasure: Optional[CodeableConcept] = None
	participantEffectivePeriod: Optional[Period] = None
	participantEffectiveDescription: Optional[str] = None
	definitionCodeableConcept: Optional[CodeableConcept] = None
	usageContext: list[UsageContext] = []
	studyEffectivePeriod: Optional[Period] = None
	participantEffectiveTimeFromStart: Optional[str] = None
	studyEffectiveDateTime: Optional[str] = None

class ResearchElementDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	variableType: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	type: str
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	characteristic: list[ResearchElementDefinition_Characteristic]
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	comment: list[str] = []
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	reviewer: list[ContactDetail] = []
	shortTitle: Optional[str] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None

