from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class CarePlan_Activity_Detail(BackboneElement):
	description: Optional[str] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	productReference: Optional[Reference] = None
	scheduledPeriod: Optional[Period] = None
	goal: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
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
	performer: Optional[List[Reference]] = None
	reasonReference: Optional[List[Reference]] = None

class CarePlan_Activity(BackboneElement):
	outcomeCodeableConcept: Optional[List[CodeableConcept]] = None
	outcomeReference: Optional[List[Reference]] = None
	progress: Optional[List[Annotation]] = None
	reference: Optional[Reference] = None
	detail: Optional[CarePlan_Activity_Detail] = None

class UsCoreCareplan(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-careplan"])
	description: Optional[str] = None
	category: List[CodeableConcept]
	addresses: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	supportingInfo: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	goal: Optional[List[Reference]] = None
	created: Optional[str] = None
	title: Optional[str] = None
	note: Optional[List[Annotation]] = None
	author: Optional[Reference] = None
	activity: Optional[List[CarePlan_Activity]] = None
	contributor: Optional[List[Reference]] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	intent: str
	replaces: Optional[List[Reference]] = None
	period: Optional[Period] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	subject: Reference
	careTeam: Optional[List[Reference]] = None
	text: Narrative
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None