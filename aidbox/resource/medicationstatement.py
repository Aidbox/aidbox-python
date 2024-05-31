from pydantic import *
from typing import Optional, List
from ..base import *

class MedicationStatement(DomainResource):
	category: Optional[CodeableConcept] = None
	dosage: Optional[List[Dosage]] = None
	derivedFrom: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	medicationCodeableConcept: Optional[CodeableConcept] = None
	statusReason: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	effectiveDateTime: Optional[str] = None
	status: str
	identifier: Optional[List[Identifier]] = None
	context: Optional[Reference] = None
	dateAsserted: Optional[str] = None
	basedOn: Optional[List[Reference]] = None
	medicationReference: Optional[Reference] = None
	partOf: Optional[List[Reference]] = None
	informationSource: Optional[Reference] = None
	subject: Reference
	effectivePeriod: Optional[Period] = None
	reasonReference: Optional[List[Reference]] = None