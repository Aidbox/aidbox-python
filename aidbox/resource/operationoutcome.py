from pydantic import *
from typing import Optional, List
from ..base import *

class OperationOutcome_Issue(BackboneElement):
	severity: str
	code: str
	details: Optional[CodeableConcept] = None
	diagnostics: Optional[str] = None
	location: Optional[List[str]] = None
	expression: Optional[List[str]] = None

class OperationOutcome(DomainResource):
	issue: List[OperationOutcome_Issue]