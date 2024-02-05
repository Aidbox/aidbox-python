from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


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
	usageContext: Optional[List[UsageContext]] = None

class Picoelement(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/picoelement"])
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
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None