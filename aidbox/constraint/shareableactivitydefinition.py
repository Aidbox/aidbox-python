from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class ActivityDefinition_Participant(BackboneElement):
	type: str
	role: Optional[CodeableConcept] = None

class ActivityDefinition_DynamicValue(BackboneElement):
	path: str
	expression: Expression

class Shareableactivitydefinition(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/shareableactivitydefinition"])
	observationResultRequirement: Optional[List[Reference]] = None
	timingRange: Optional[Range] = None
	description: str
	date: Optional[str] = None
	transform: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: str
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	dosage: Optional[List[str]] = None
	observationRequirement: Optional[List[Reference]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	name: str
	productReference: Optional[Reference] = None
	timingPeriod: Optional[Period] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: bool
	topic: Optional[List[CodeableConcept]] = None
	participant: Optional[List[ActivityDefinition_Participant]] = None
	title: Optional[str] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	usage: Optional[str] = None
	timingDuration: Optional[str] = None
	priority: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	kind: Optional[str] = None
	dynamicValue: Optional[List[ActivityDefinition_DynamicValue]] = None
	url: str
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	doNotPerform: Optional[bool] = None
	bodySite: Optional[List[CodeableConcept]] = None
	timingAge: Optional[str] = None
	intent: Optional[str] = None
	specimenRequirement: Optional[List[Reference]] = None
	reviewer: Optional[List[ContactDetail]] = None
	quantity: Optional[Quantity] = None
	version: str
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	location: Optional[Reference] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	profile: Optional[str] = None
	effectivePeriod: Optional[Period] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None