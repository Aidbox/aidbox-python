from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class MedicationAdministration_Dosage(BackboneElement):
	text: Optional[str] = None
	site: Optional[CodeableConcept] = None
	route: Optional[CodeableConcept] = None
	method: Optional[CodeableConcept] = None
	dose: Optional[Quantity] = None
	rateRatio: Optional[Ratio] = None
	rateQuantity: Optional[Quantity] = None

class MedicationAdministration_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference

class McodeCancerRelatedMedicationAdministration(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-cancer-related-medication-administration"])
	category: Optional[CodeableConcept] = None
	request: Optional[Reference] = None
	eventHistory: Optional[List[Reference]] = None
	dosage: Optional[MedicationAdministration_Dosage] = None
	instantiates: Optional[List[str]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	supportingInformation: Optional[List[Reference]] = None
	effectiveDateTime: Optional[str] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	context: Optional[Reference] = None
	device: Optional[List[Reference]] = None
	medicationReference: Optional[Reference] = None
	partOf: Optional[List[Reference]] = None
	subject: Reference
	performer: Optional[List[MedicationAdministration_Performer]] = None
	effectivePeriod: Optional[Period] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None