from typing import Optional
from base import *

class MedicationStatement(DomainResource):
	category: Optional[CodeableConcept] = None
	dosage: list[str] = []
	derivedFrom: list[Reference] = []
	reasonCode: list[CodeableConcept] = []
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: list[CodeableConcept] = []
	note: list[Annotation] = []
	effectiveDateTime: Optional[str] = None
	status: str
	identifier: list[Identifier] = []
	context: Optional[Reference] = None
	dateAsserted: Optional[str] = None
	basedOn: list[Reference] = []
	medicationReference: Optional[Reference] = None
	partOf: list[Reference] = []
	informationSource: Optional[Reference] = None
	subject: Reference
	effectivePeriod: Optional[Period] = None
	reasonReference: list[Reference] = []

