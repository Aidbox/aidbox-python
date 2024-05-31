from pydantic import *
from typing import Optional, List, Literal
from ..base import *

class Goal_Target(BackboneElement):
	detailRange: Optional[Range] = None
	detailQuantity: Optional[Quantity] = None
	detailInteger: Optional[int] = None
	detailString: Optional[str] = None
	measure: Optional[CodeableConcept] = None
	detailRatio: Optional[Ratio] = None
	detailCodeableConcept: Optional[CodeableConcept] = None
	dueDate: Optional[str] = None
	detailBoolean: Optional[bool] = None
	dueDuration: Optional[Duration] = None

class UsCoreGoal(DomainResource):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-goal"])
	description: CodeableConcept
	category: Optional[List[CodeableConcept]] = None
	addresses: Optional[List[Reference]] = None
	expressedBy: Optional[Reference] = None
	startDate: Optional[str] = None
	achievementStatus: Optional[CodeableConcept] = None
	statusReason: Optional[str] = None
	note: Optional[List[Annotation]] = None
	startCodeableConcept: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	outcomeCode: Optional[List[CodeableConcept]] = None
	identifier: Optional[List[Identifier]] = None
	statusDate: Optional[str] = None
	target: Optional[List[Goal_Target]] = None
	outcomeReference: Optional[List[Reference]] = None
	subject: Reference
	lifecycleStatus: str