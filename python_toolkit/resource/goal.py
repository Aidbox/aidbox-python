from typing import Optional
from base import *

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
	dueDuration: Optional[str] = None

class Goal(DomainResource):
	description: CodeableConcept
	category: list[CodeableConcept] = []
	addresses: list[Reference] = []
	expressedBy: Optional[Reference] = None
	startDate: Optional[str] = None
	achievementStatus: Optional[CodeableConcept] = None
	statusReason: Optional[str] = None
	note: list[Annotation] = []
	startCodeableConcept: Optional[CodeableConcept] = None
	priority: Optional[CodeableConcept] = None
	outcomeCode: list[CodeableConcept] = []
	identifier: list[Identifier] = []
	statusDate: Optional[str] = None
	target: list[Goal_Target] = []
	outcomeReference: list[Reference] = []
	subject: Reference
	lifecycleStatus: str

