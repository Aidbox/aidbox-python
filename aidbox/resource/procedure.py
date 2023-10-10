from typing import Optional
from ..base import *

class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None
	onBehalfOf: Optional[Reference] = None

class Procedure(DomainResource):
	category: Optional[CodeableConcept] = None
	report: list[Reference] = []
	usedCode: list[CodeableConcept] = []
	usedReference: list[Reference] = []
	instantiatesCanonical: list[str] = []
	instantiatesUri: list[str] = []
	focalDevice: list[Procedure_FocalDevice] = []
	encounter: Optional[Reference] = None
	performedAge: Optional[str] = None
	complicationDetail: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	performedString: Optional[str] = None
	statusReason: Optional[CodeableConcept] = None
	outcome: Optional[CodeableConcept] = None
	asserter: Optional[Reference] = None
	note: list[Annotation] = []
	performedRange: Optional[Range] = None
	complication: list[CodeableConcept] = []
	status: str
	performedDateTime: Optional[str] = None
	recorder: Optional[Reference] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	bodySite: list[CodeableConcept] = []
	basedOn: list[Reference] = []
	partOf: list[Reference] = []
	performedPeriod: Optional[Period] = None
	location: Optional[Reference] = None
	followUp: list[CodeableConcept] = []
	subject: Reference
	performer: list[Procedure_Performer] = []
	reasonReference: list[Reference] = []

