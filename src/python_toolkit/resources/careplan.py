from typing import Optional
from base import *

class CarePlan_Activity_Detail(BackboneElement):
	description: Optional[str] = None
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	productCodeableConcept: Optional[CodeableConcept] = None
	productReference: Optional[Reference] = None
	scheduledPeriod: Optional[Period] = None
	goal: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	statusReason: Optional[CodeableConcept] = None
	scheduledTiming: Optional[str] = None
	dailyAmount: Optional[Quantity] = None
	scheduledString: Optional[str] = None
	status: str
	kind: Optional[str] = None
	code: Optional[CodeableConcept] = None
	doNotPerform: Optional[bool] = None
	quantity: Optional[Quantity] = None
	location: Optional[Reference] = None
	performer: list[Reference] = []
	reasonReference: list[Reference] = []

class CarePlan_Activity(BackboneElement):
	detail: Optional[CarePlan_Activity_Detail] = None
	outcomeCodeableConcept: list[CodeableConcept] = []
	outcomeReference: list[Reference] = []
	progress: list[Annotation] = []
	reference: Optional[Reference] = None

class CarePlan(DomainResource):
	description: Optional[str] = None
	category: list[CodeableConcept] = []
	addresses: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	supportingInfo: list[Reference] = []
	encounter: Optional[Reference] = None
	goal: list[Reference] = []
	created: Optional[str] = None
	title: Optional[str] = None
	note: list[Annotation] = []
	author: Optional[Reference] = None
	activity: list[CarePlan_Activity] = []
	contributor: list[Reference] = []
	status: str
	identifier: list[Identifier] = []
	intent: str
	replaces: list[Reference] = []
	period: Optional[Period] = None
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	subject: Reference
	careTeam: list[Reference] = []

