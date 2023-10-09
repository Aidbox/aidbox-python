from typing import Optional
from base import *

class OperationOutcome_Issue(BackboneElement):
	code: str
	details: Optional[CodeableConcept] = None
	diagnostics: Optional[str] = None
	expression: list[str] = []
	location: list[str] = []
	severity: str

class OperationOutcome(DomainResource):
	issue: list[OperationOutcome_Issue]

