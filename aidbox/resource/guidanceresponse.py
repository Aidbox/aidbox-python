from pydantic import *
from typing import Optional, List
from ..base import *

class GuidanceResponse(DomainResource):
	dataRequirement: Optional[List[DataRequirement]] = None
	moduleCanonical: Optional[str] = None
	encounter: Optional[Reference] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	outputParameters: Optional[Reference] = None
	evaluationMessage: Optional[List[Reference]] = None
	requestIdentifier: Optional[Identifier] = None
	note: Optional[List[Annotation]] = None
	status: str
	result: Optional[Reference] = None
	identifier: Optional[List[Identifier]] = None
	moduleCodeableConcept: Optional[CodeableConcept] = None
	moduleUri: Optional[str] = None
	occurrenceDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	performer: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None