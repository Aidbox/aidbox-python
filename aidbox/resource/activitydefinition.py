from pydantic import *
from typing import Optional, List
from ..base import *

class ActivityDefinition_Participant(BackboneElement):
	type: str
	role: Optional[CodeableConcept] = None

class ActivityDefinition_DynamicValue(BackboneElement):
	path: str
	expression: Expression

class ActivityDefinition(DomainResource):
	observationResultRequirement: Optional[List[Reference]] = None
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	date: Optional[str] = None
	transform: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	dosage: Optional[List[Dosage]] = None
	observationRequirement: Optional[List[Reference]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	productReference: Optional[Reference] = None
	timingPeriod: Optional[Period] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	topic: Optional[List[CodeableConcept]] = None
	participant: Optional[List[ActivityDefinition_Participant]] = None
	title: Optional[str] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[Timing] = None
	usage: Optional[str] = None
	timingDuration: Optional[Duration] = None
	priority: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	kind: Optional[str] = None
	dynamicValue: Optional[List[ActivityDefinition_DynamicValue]] = None
	url: Optional[str] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	doNotPerform: Optional[bool] = None
	bodySite: Optional[List[CodeableConcept]] = None
	timingAge: Optional[Age] = None
	intent: Optional[str] = None
	specimenRequirement: Optional[List[Reference]] = None
	reviewer: Optional[List[ContactDetail]] = None
	quantity: Optional[Quantity] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	location: Optional[Reference] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	profile: Optional[str] = None
	effectivePeriod: Optional[Period] = None