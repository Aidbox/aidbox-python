from typing import Optional
from ..base import *

class RequestGroup_Action_RelatedAction(BackboneElement):
	actionId: str
	offsetDuration: Optional[str] = None
	offsetRange: Optional[Range] = None
	relationship: str

class RequestGroup_Action_Condition(BackboneElement):
	expression: Optional[Expression] = None
	kind: str

class RequestGroup_Action(BackboneElement):
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	textEquivalent: Optional[str] = None
	timingPeriod: Optional[Period] = None
	relatedAction: list[RequestGroup_Action_RelatedAction] = []
	type: Optional[CodeableConcept] = None
	participant: list[Reference] = []
	title: Optional[str] = None
	documentation: list[RelatedArtifact] = []
	prefix: Optional[str] = None
	selectionBehavior: Optional[str] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	timingDuration: Optional[str] = None
	priority: Optional[str] = None
	requiredBehavior: Optional[str] = None
	condition: list[RequestGroup_Action_Condition] = []
	resource: Optional[Reference] = None
	groupingBehavior: Optional[str] = None
	code: list[CodeableConcept] = []
	timingAge: Optional[str] = None
	action: list[str] = []
	precheckBehavior: Optional[str] = None
	cardinalityBehavior: Optional[str] = None

class RequestGroup(DomainResource):
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	encounter: Optional[Reference] = None
	reasonCode: list[CodeableConcept] = []
	authoredOn: Optional[str] = None
	note: list[Annotation] = []
	author: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	intent: str
	action: list[RequestGroup_Action] = []
	replaces: list[Reference] = []
	basedOn: list[Reference] = []
	subject: Optional[Reference] = None
	reasonReference: list[Reference] = []

