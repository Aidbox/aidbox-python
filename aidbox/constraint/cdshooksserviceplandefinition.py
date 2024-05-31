from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class PlanDefinition_Goal_Target(BackboneElement):
	measure: Optional[CodeableConcept] = None
	detailQuantity: Optional[Quantity] = None
	detailRange: Optional[Range] = None
	detailCodeableConcept: Optional[CodeableConcept] = None
	due: Optional[Duration] = None

class PlanDefinition_Goal(BackboneElement):
	category: Optional[CodeableConcept] = None
	description: CodeableConcept
	priority: Optional[CodeableConcept] = None
	start: Optional[CodeableConcept] = None
	addresses: Optional[List[CodeableConcept]] = None
	documentation: Optional[List[RelatedArtifact]] = None
	target: Optional[List[PlanDefinition_Goal_Target]] = None

class PlanDefinition_Action_RelatedAction(BackboneElement):
	actionId: str
	relationship: str
	offsetDuration: Optional[Duration] = None
	offsetRange: Optional[Range] = None

class PlanDefinition_Action_Participant(BackboneElement):
	type: str
	role: Optional[CodeableConcept] = None

class PlanDefinition_Action_Condition(BackboneElement):
	kind: str
	expression: Optional[Expression] = None

class PlanDefinition_Action_DynamicValue(BackboneElement):
	path: Optional[str] = None
	expression: Optional[Expression] = None

class PlanDefinition_Action(BackboneElement):
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	transform: Optional[str] = None
	textEquivalent: Optional[str] = None
	definitionUri: Optional[str] = None
	goalId: Optional[List[str]] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	timingPeriod: Optional[Period] = None
	definitionCanonical: Optional[str] = None
	relatedAction: Optional[List[PlanDefinition_Action_RelatedAction]] = None
	type: Optional[CodeableConcept] = None
	participant: Optional[List[PlanDefinition_Action_Participant]] = None
	output: Optional[List[DataRequirement]] = None
	title: Optional[str] = None
	documentation: Optional[List[RelatedArtifact]] = None
	prefix: Optional[str] = None
	selectionBehavior: Optional[str] = None
	reason: Optional[List[CodeableConcept]] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[Timing] = None
	timingDuration: Optional[Duration] = None
	priority: Optional[str] = None
	requiredBehavior: Optional[str] = None
	condition: Optional[List[PlanDefinition_Action_Condition]] = None
	groupingBehavior: Optional[str] = None
	dynamicValue: Optional[List[PlanDefinition_Action_DynamicValue]] = None
	code: Optional[List[CodeableConcept]] = None
	timingAge: Optional[Age] = None
	action: Optional[List[str]] = None
	precheckBehavior: Optional[str] = None
	input: Optional[List[DataRequirement]] = None
	trigger: Optional[List[TriggerDefinition]] = None
	subjectReference: Optional[Reference] = None
	cardinalityBehavior: Optional[str] = None

class Cdshooksserviceplandefinition(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/cdshooksserviceplandefinition"])
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: Optional[List[ContactDetail]] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: Optional[List[UsageContext]] = None
	goal: Optional[List[PlanDefinition_Goal]] = None
	copyright: Optional[str] = None
	type: Optional[CodeableConcept] = None
	experimental: Optional[bool] = None
	topic: Optional[List[CodeableConcept]] = None
	title: Optional[str] = None
	library: Optional[List[str]] = None
	author: Optional[List[ContactDetail]] = None
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	editor: Optional[List[ContactDetail]] = None
	action: Optional[List[PlanDefinition_Action]] = None
	reviewer: Optional[List[ContactDetail]] = None
	version: Optional[str] = None
	relatedArtifact: Optional[List[RelatedArtifact]] = None
	contact: Optional[List[ContactDetail]] = None
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None