from typing import Optional
from ..base import *

class Specimen_Processing(BackboneElement):
	additive: list[Reference] = []
	description: Optional[str] = None
	procedure: Optional[CodeableConcept] = None
	timeDateTime: Optional[str] = None
	timePeriod: Optional[Period] = None

class Specimen_Container(BackboneElement):
	additiveCodeableConcept: Optional[CodeableConcept] = None
	additiveReference: Optional[Reference] = None
	capacity: Optional[Quantity] = None
	description: Optional[str] = None
	identifier: list[Identifier] = []
	specimenQuantity: Optional[Quantity] = None
	type: Optional[CodeableConcept] = None

class Specimen_Collection(BackboneElement):
	collectedDateTime: Optional[str] = None
	fastingStatusCodeableConcept: Optional[CodeableConcept] = None
	method: Optional[CodeableConcept] = None
	fastingStatusDuration: Optional[str] = None
	duration: Optional[str] = None
	collector: Optional[Reference] = None
	bodySite: Optional[CodeableConcept] = None
	quantity: Optional[Quantity] = None
	collectedPeriod: Optional[Period] = None

class Specimen(DomainResource):
	request: list[Reference] = []
	receivedTime: Optional[str] = None
	processing: list[Specimen_Processing] = []
	parent: list[Reference] = []
	type: Optional[CodeableConcept] = None
	note: list[Annotation] = []
	status: Optional[str] = None
	condition: list[CodeableConcept] = []
	container: list[Specimen_Container] = []
	identifier: list[Identifier] = []
	accessionIdentifier: Optional[Identifier] = None
	collection: Optional[Specimen_Collection] = None
	subject: Optional[Reference] = None

