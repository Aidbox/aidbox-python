from pydantic import *
from typing import Optional, List
from ..base import *

class Flag(DomainResource):
	identifier: Optional[List[Identifier]] = None
	status: str
	category: Optional[List[CodeableConcept]] = None
	code: CodeableConcept
	subject: Reference
	period: Optional[Period] = None
	encounter: Optional[Reference] = None
	author: Optional[Reference] = None