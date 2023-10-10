from typing import Optional
from ..base import *

class PlanDefinition_Goal_Target(BackboneElement):
	detailCodeableConcept: Optional[CodeableConcept] = None
	detailQuantity: Optional[Quantity] = None
	detailRange: Optional[Range] = None
	due: Optional[str] = None
	measure: Optional[CodeableConcept] = None

class PlanDefinition_Goal(BackboneElement):
	addresses: list[CodeableConcept] = []
	category: Optional[CodeableConcept] = None
	description: CodeableConcept
	documentation: list[RelatedArtifact] = []
	priority: Optional[CodeableConcept] = None
	start: Optional[CodeableConcept] = None
	target: list[PlanDefinition_Goal_Target] = []

class PlanDefinition_Action_RelatedAction(BackboneElement):
	actionId: str
	offsetDuration: Optional[str] = None
	offsetRange: Optional[Range] = None
	relationship: str

class PlanDefinition_Action_Participant(BackboneElement):
	role: Optional[CodeableConcept] = None
	type: str

class PlanDefinition_Action_Condition(BackboneElement):
	expression: Optional[Expression] = None
	kind: str

class PlanDefinition_Action_DynamicValue(BackboneElement):
	expression: Optional[Expression] = None
	path: Optional[str] = None

class PlanDefinition_Action(BackboneElement):
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	transform: Optional[str] = None
	textEquivalent: Optional[str] = None
	definitionUri: Optional[str] = None
	goalId: list[str] = []
	subjectCodeableConcept: Optional[CodeableConcept] = None
	timingPeriod: Optional[Period] = None
	definitionCanonical: Optional[str] = None
	relatedAction: list[PlanDefinition_Action_RelatedAction] = []
	type: Optional[CodeableConcept] = None
	participant: list[PlanDefinition_Action_Participant] = []
	output: list[DataRequirement] = []
	title: Optional[str] = None
	documentation: list[RelatedArtifact] = []
	prefix: Optional[str] = None
	selectionBehavior: Optional[str] = None
	reason: list[CodeableConcept] = []
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	timingDuration: Optional[str] = None
	priority: Optional[str] = None
	requiredBehavior: Optional[str] = None
	condition: list[PlanDefinition_Action_Condition] = []
	groupingBehavior: Optional[str] = None
	dynamicValue: list[PlanDefinition_Action_DynamicValue] = []
	code: list[CodeableConcept] = []
	timingAge: Optional[str] = None
	action: list[str] = []
	precheckBehavior: Optional[str] = None
	input: list[DataRequirement] = []
	trigger: list[TriggerDefinition] = []
	subjectReference: Optional[Reference] = None
	cardinalityBehavior: Optional[str] = None

class PlanDefinition(DomainResource):
	description: Optional[str] = None
	date: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	useContext: list[UsageContext] = []
	goal: list[PlanDefinition_Goal] = []
	copyright: Optional[str] = None
	type: Optional[CodeableConcept] = None
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	usage: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	url: Optional[str] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	action: list[PlanDefinition_Action] = []
	reviewer: list[ContactDetail] = []
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	effectivePeriod: Optional[Period] = None

