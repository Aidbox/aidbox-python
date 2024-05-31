from pydantic import *
from typing import Optional, List
from ..base import *

class RequestGroup_Action_RelatedAction(BackboneElement):
	actionId: str
	relationship: str
	offsetDuration: Optional[Duration] = None
	offsetRange: Optional[Range] = None

class RequestGroup_Action_Condition(BackboneElement):
	kind: str
	expression: Optional[Expression] = None

class RequestGroup_Action(BackboneElement):
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	textEquivalent: Optional[str] = None
	timingPeriod: Optional[Period] = None
	relatedAction: Optional[List[RequestGroup_Action_RelatedAction]] = None
	type: Optional[CodeableConcept] = None
	participant: Optional[List[Reference]] = None
	title: Optional[str] = None
	documentation: Optional[List[RelatedArtifact]] = None
	prefix: Optional[str] = None
	selectionBehavior: Optional[str] = None
	timingDateTime: Optional[str] = None
	timingTiming: Optional[Timing] = None
	timingDuration: Optional[Duration] = None
	priority: Optional[str] = None
	requiredBehavior: Optional[str] = None
	condition: Optional[List[RequestGroup_Action_Condition]] = None
	resource: Optional[Reference] = None
	groupingBehavior: Optional[str] = None
	code: Optional[List[CodeableConcept]] = None
	timingAge: Optional[Age] = None
	action: Optional[List[str]] = None
	precheckBehavior: Optional[str] = None
	cardinalityBehavior: Optional[str] = None

class RequestGroup(DomainResource):
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	encounter: Optional[Reference] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	authoredOn: Optional[str] = None
	note: Optional[List[Annotation]] = None
	author: Optional[Reference] = None
	priority: Optional[str] = None
	status: str
	groupIdentifier: Optional[Identifier] = None
	code: Optional[CodeableConcept] = None
	identifier: Optional[List[Identifier]] = None
	intent: str
	action: Optional[List[RequestGroup_Action]] = None
	replaces: Optional[List[Reference]] = None
	basedOn: Optional[List[Reference]] = None
	subject: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None