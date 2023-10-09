from typing import Optional
from base import *

class MedicationAdministration_Dosage(BackboneElement):
	dose: Optional[Quantity] = None
	method: Optional[CodeableConcept] = None
	rateQuantity: Optional[Quantity] = None
	rateRatio: Optional[Ratio] = None
	route: Optional[CodeableConcept] = None
	site: Optional[CodeableConcept] = None
	text: Optional[str] = None

class MedicationAdministration_Performer(BackboneElement):
	actor: Reference
	function: Optional[CodeableConcept] = None

class MedicationAdministration(DomainResource):
	category: Optional[CodeableConcept] = None
	request: Optional[Reference] = None
	eventHistory: list[Reference] = []
	dosage: Optional[MedicationAdministration_Dosage] = None
	instantiates: list[str] = []
	reasonCode: list[CodeableConcept] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: list[CodeableConcept] = []
	note: list[Annotation] = []
	supportingInformation: list[Reference] = []
	effectiveDateTime: Optional[str] = None
	status: str
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	device: list[Reference] = []
	medicationReference: Optional[Reference] = None
	partOf: list[Reference] = []
	subject: Reference
	performer: list[MedicationAdministration_Performer] = []
	effectivePeriod: Optional[Period] = None
	reasonReference: list[Reference] = []

