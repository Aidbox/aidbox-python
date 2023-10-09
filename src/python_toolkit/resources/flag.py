from typing import Optional
from base import *

class Flag(DomainResource):
	author: Optional[Reference] = None
	category: list[CodeableConcept] = []
	code: CodeableConcept
	encounter: Optional[Reference] = None
	identifier: list[Identifier] = []
	period: Optional[Period] = None
	status: str
	subject: Reference

